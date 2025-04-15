from salesforce.client import SalesforceClient
import grpc
import ssl
import argparse
from google.protobuf import wrappers_pb2
from case_management_service.salesforce import salesforce_pb2
from case_management_service.salesforce import salesforce_pb2_grpc
from case_management_service import common_pb2
import re
from collections import Counter
import os
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import torch

def get_email_status_description(status_value):
    """Convert the numeric status value to a human-readable description."""
    status_map = {
        0: "Unspecified",
        1: "New",
        2: "Read",
        3: "Replied",
        4: "Sent",
        5: "Forwarded",
        6: "Draft"
    }
    return status_map.get(status_value, f"Unknown ({status_value})")

# Initialize sentiment analyzer (will be loaded once)
sentiment_analyzer = None
emotion_analyzer = None

def load_models():
    """Load the sentiment and emotion analysis models."""
    global sentiment_analyzer, emotion_analyzer
    
    if sentiment_analyzer is None:
        print("Loading sentiment analysis model...")
        sentiment_analyzer = pipeline(
            "sentiment-analysis",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            device=0 if torch.cuda.is_available() else -1
        )
    
    if emotion_analyzer is None:
        print("Loading emotion analysis model...")
        emotion_analyzer = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            device=0 if torch.cuda.is_available() else -1
        )

def analyze_sentiment_with_free_llm(text, email_date=None):
    """Analyze the sentiment of a text using a free Hugging Face model."""
    if not text:
        return 0, "Neutral", None
    
    # Load models if not already loaded
    load_models()
    
    # Clean the text by removing HTML tags and extra whitespace
    clean_text = re.sub(r'<[^>]+>', '', text)
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    # Truncate text if it's too long (to stay within token limits)
    max_length = 512  # Adjust based on model's context window
    if len(clean_text) > max_length:
        clean_text = clean_text[:max_length] + "..."
    
    try:
        # Get sentiment analysis
        sentiment_result = sentiment_analyzer(clean_text)[0]
        sentiment_label = sentiment_result['label']
        sentiment_score = sentiment_result['score']
        
        # Convert sentiment to our scale (-1 to 1)
        if sentiment_label == 'NEGATIVE':
            normalized_score = -sentiment_score
        else:  # POSITIVE
            normalized_score = sentiment_score
        
        # Get emotion analysis
        emotion_result = emotion_analyzer(clean_text)[0]
        emotion_label = emotion_result['label']
        emotion_score = emotion_result['score']
        
        # Map sentiment to our categories
        if normalized_score > 0.6:
            category = "Very Positive"
        elif normalized_score > 0.2:
            category = "Positive"
        elif normalized_score > 0:
            category = "Slightly Positive"
        elif normalized_score > -0.2:
            category = "Neutral"
        elif normalized_score > -0.6:
            category = "Slightly Negative"
        elif normalized_score > -0.8:
            category = "Negative"
        else:
            category = "Very Negative"
        
        # Create explanation
        explanation = f"The text expresses {emotion_label.lower()} emotion with {sentiment_label.lower()} sentiment."
        
        return normalized_score, category, {
            "emotions": emotion_label,
            "explanation": explanation
        }
        
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return 0, "Neutral", None

def plot_sentiment_trend(sentiment_data):
    """Create a plot showing sentiment changes over time."""
    if not sentiment_data:
        return
    
    # Extract data for plotting
    dates = [item['date'] for item in sentiment_data]
    scores = [item['score'] for item in sentiment_data]
    categories = [item['category'] for item in sentiment_data]
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    
    # Plot sentiment scores
    plt.plot(dates, scores, 'b-o', linewidth=2, markersize=8)
    
    # Add category labels
    for i, (date, score, category) in enumerate(zip(dates, scores, categories)):
        plt.annotate(category, (date, score), 
                    textcoords="offset points", 
                    xytext=(0,10), 
                    ha='center',
                    fontsize=8)
    
    # Customize the plot
    plt.title('Merchant Sentiment Over Time', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Sentiment Score', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Set y-axis limits
    plt.ylim(-1.2, 1.2)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Add a horizontal line at y=0
    plt.axhline(y=0, color='r', linestyle='--', alpha=0.3)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('sentiment_trend.png')
    plt.close()

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Salesforce case and email operations')
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # Case lookup command
    case_parser = subparsers.add_parser('case', help='Get Salesforce case details by case number')
    case_parser.add_argument('case_number', help='The case number to look up')
    
    # Email audit command with case number
    email_parser = subparsers.add_parser('audit_emails', help='Get Salesforce emails for a case number')
    email_parser.add_argument('case_number', help='The case number to look up emails for')
    
    args = parser.parse_args()
    
    # Create metadata credentials
    api_secret = 'KGCu_nYudn_hdhjNn5UDRO2pnSX7kkjgS88cOCZ62j2R2X8My4eI9Brb3dS0E2MNu5OD_MzXyXAbceYsBiWPmDK7ksrq2S5eFwR2obebzu1zgiD19kM5f1gBG6Dh7Ehwd_OdIhssGcfNV_m9LkGUBXVeijUkQAdzASPl4pB-dGY'
    
    # Create channel options
    channel_options = [
        ('grpc.max_receive_message_length', 100 * 1024 * 1024),  # 100MB
    ]
    
    print("Creating SalesforceClient...")
    # Create a client instance with insecure connection
    with SalesforceClient(
        host="localhost",
        port=50051,
        use_ssl=False,
        channel_options=channel_options
    ) as client:
        # Create metadata for each call
        metadata = [
            ('dd-api-secret', api_secret)
        ]
        
        if args.command == 'case':
            # Case lookup functionality
            case_number = args.case_number
            
            print("\n" + "="*50)
            print(f"Trying case number: {case_number}")
            print("="*50)
            
            try:
                # Create the request with the case number
                case_request = salesforce_pb2.GetSalesforceCasesByCaseNumberRequest(
                    case_number=wrappers_pb2.StringValue(value=case_number)
                )
                
                # Make the call
                case_response = client.stub.GetSalesforceCasesByCaseNumber(
                    case_request,
                    metadata=metadata,
                    timeout=30.0
                )
                
                if case_response.HasField('salesforce_case'):
                    case = case_response.salesforce_case
                    print("\nCase Details:")
                    print(f"Case Number: {case_number}")  # Using the input case number
                    
                    # Print all available fields
                    print("\nAvailable fields in the response:")
                    for field in case.DESCRIPTOR.fields:
                        field_name = field.name
                        if case.HasField(field_name):
                            field_value = getattr(case, field_name)
                            if hasattr(field_value, 'value'):
                                print(f"{field_name}: {field_value.value}")
                            else:
                                print(f"{field_name}: {field_value}")
                else:
                    print("No case found with the given case number")
                    
            except Exception as e:
                print(f"Error occurred for case {case_number}: {e}")
                if isinstance(e, grpc.RpcError):
                    print(f"Status code: {e.code()}")
                    print(f"Details: {e.details()}")
        
        elif args.command == 'audit_emails':
            # Email audit functionality with case number
            case_number = args.case_number
            
            print("\n" + "="*50)
            print(f"Looking up case ID for case number: {case_number}")
            print("="*50)
            
            # Variables for summary statistics
            support_emails = 0
            merchant_emails = 0
            merchant_sentiments = []
            merchant_texts = []
            sentiment_timeline = []
            
            try:
                # First, get the case ID from the case number
                case_request = salesforce_pb2.GetSalesforceCasesByCaseNumberRequest(
                    case_number=wrappers_pb2.StringValue(value=case_number)
                )
                
                # Make the call to get case details
                case_response = client.stub.GetSalesforceCasesByCaseNumber(
                    case_request,
                    metadata=metadata,
                    timeout=30.0
                )
                
                if case_response.HasField('salesforce_case'):
                    # Extract the case ID from the response
                    case = case_response.salesforce_case
                    case_id = None
                    
                    # Find the case_id field in the response
                    for field in case.DESCRIPTOR.fields:
                        if field.name == 'case' and case.HasField('case'):
                            case_details = getattr(case, 'case')
                            for detail_field in case_details.DESCRIPTOR.fields:
                                if detail_field.name == 'case_id' and case_details.HasField('case_id'):
                                    case_id = getattr(case_details, 'case_id').value
                                    break
                    
                    if case_id:
                        print(f"Found case ID: {case_id}")
                        
                        # Now fetch the emails using the case ID
                        print("\n" + "="*50)
                        print(f"Fetching emails for case ID: {case_id}")
                        print("="*50)
                        
                        # Create the request with the case ID
                        email_request = salesforce_pb2.GetSalesforceEmailsRequest(
                            salesforce_case_ids=[wrappers_pb2.StringValue(value=case_id)]
                        )
                        
                        # Make the call to get emails
                        email_response = client.stub.GetSalesforceEmails(
                            email_request,
                            metadata=metadata,
                            timeout=30.0
                        )
                        
                        # Process and display email data
                        if email_response.emails:
                            print(f"\nFound {len(email_response.emails)} emails for case number: {case_number} (ID: {case_id})")
                            for i, email in enumerate(email_response.emails, 1):
                                print(f"\nEmail #{i}:")
                                
                                # Extract sender information for summary
                                from_email = None
                                from_address = None
                                text_body = None
                                email_date = None
                                
                                for field in email.DESCRIPTOR.fields:
                                    field_name = field.name
                                    # Skip fields that don't have presence information or are too noisy
                                    if field_name in ['status', 'attachments', 'html_body']:
                                        if field_name == 'attachments':
                                            # For attachments, show the count
                                            field_value = getattr(email, field_name)
                                            print(f"{field_name}: {len(field_value)} items")
                                        elif field_name == 'status':
                                            # For status, show a descriptive value
                                            status_value = getattr(email, field_name)
                                            status_desc = get_email_status_description(status_value)
                                            print(f"{field_name}: {status_desc}")
                                        continue
                                    
                                    # For other fields, check if they have presence information
                                    if hasattr(email, 'HasField') and email.HasField(field_name):
                                        field_value = getattr(email, field_name)
                                        if hasattr(field_value, 'value'):
                                            value = field_value.value
                                            print(f"{field_name}: {value}")
                                            
                                            # Store from_email, from_address, text_body, and date for summary
                                            if field_name == 'from_email':
                                                from_email = value
                                            elif field_name == 'from_address':
                                                from_address = value
                                            elif field_name == 'text_body':
                                                text_body = value
                                            elif field_name == 'created_date':
                                                email_date = value
                                        else:
                                            print(f"{field_name}: {field_value}")
                                
                                # Update summary statistics
                                # Use from_address if available, otherwise fall back to from_email
                                sender_address = from_address if from_address else from_email
                                
                                if sender_address:  # Only need sender address for categorization
                                    print(f"DEBUG: Processing email from: '{sender_address}'")  # Added quotes to see exact string
                                    print(f"DEBUG: After strip and lower: '{sender_address.strip().lower()}'")  # Show processed value
                                    print(f"DEBUG: Comparison result: {sender_address.strip().lower() == 'support@doordash.com'}")  # Show comparison result
                                    
                                    if sender_address.strip().lower() == "support@doordash.com":
                                        support_emails += 1
                                        print(f"DEBUG: Counted as support email. Total: {support_emails}")
                                    else:
                                        merchant_emails += 1
                                        print(f"DEBUG: Counted as merchant email from: {sender_address}")
                                        # Only perform sentiment analysis on merchant emails with text body
                                        if text_body and text_body.strip():  # Ensure text_body exists and is not empty
                                            print(f"DEBUG: Adding merchant text for sentiment analysis. Length: {len(text_body)}")
                                            merchant_texts.append(text_body)
                                            sentiment_score, sentiment_category, sentiment_details = analyze_sentiment_with_free_llm(text_body, email_date)
                                            print(f"DEBUG: Sentiment analysis result: {sentiment_category} (score: {sentiment_score})")
                                            merchant_sentiments.append(sentiment_category)
                                            
                                            # Add to sentiment timeline
                                            if email_date:
                                                try:
                                                    parsed_date = datetime.fromisoformat(email_date.replace('Z', '+00:00'))
                                                    sentiment_timeline.append({
                                                        'date': parsed_date,
                                                        'score': sentiment_score,
                                                        'category': sentiment_category,
                                                        'details': sentiment_details
                                                    })
                                                    print(f"DEBUG: Added to sentiment timeline. Total entries: {len(sentiment_timeline)}")
                                                except Exception as e:
                                                    print(f"DEBUG: Error parsing date {email_date}: {e}")
                            
                            # Sort sentiment timeline by date
                            sentiment_timeline.sort(key=lambda x: x['date'])
                            
                            # Print summary section
                            print("\n" + "="*50)
                            print("EMAIL SUMMARY")
                            print("="*50)
                            
                            # Email statistics
                            print(f"\nEmail Statistics:")
                            print(f"Total Emails: {len(email_response.emails)}")
                            print(f"Support Emails: {support_emails}")
                            print(f"Merchant Emails: {merchant_emails}")
                            print(f"DEBUG: Merchant texts collected: {len(merchant_texts)}")
                            print(f"DEBUG: Merchant sentiments collected: {len(merchant_sentiments)}")
                            
                            # Sentiment analysis
                            if merchant_sentiments:
                                print(f"\nMerchant Sentiment Analysis:")
                                sentiment_counts = Counter(merchant_sentiments)
                                total_sentiments = len(merchant_sentiments)
                                
                                for sentiment, count in sentiment_counts.items():
                                    percentage = (count / total_sentiments) * 100
                                    print(f"{sentiment}: {count} emails ({percentage:.1f}%)")
                                
                                # Overall sentiment
                                most_common_sentiment = sentiment_counts.most_common(1)[0][0]
                                print(f"\nOverall Merchant Sentiment: {most_common_sentiment}")
                                
                                # Calculate average sentiment score
                                if merchant_texts:
                                    total_score = sum(analyze_sentiment_with_free_llm(text)[0] for text in merchant_texts)
                                    avg_score = total_score / len(merchant_texts)
                                    print(f"Average Sentiment Score: {avg_score:.2f} (range: -1.0 to 1.0)")
                                
                                # Sentiment trend analysis
                                if len(sentiment_timeline) >= 2:
                                    print("\nSentiment Trend Analysis:")
                                    first_sentiment = sentiment_timeline[0]
                                    last_sentiment = sentiment_timeline[-1]
                                    
                                    sentiment_change = last_sentiment['score'] - first_sentiment['score']
                                    if sentiment_change > 0.2:
                                        trend = "IMPROVED significantly"
                                    elif sentiment_change > 0:
                                        trend = "slightly improved"
                                    elif sentiment_change < -0.2:
                                        trend = "DEGRADED significantly"
                                    elif sentiment_change < 0:
                                        trend = "slightly degraded"
                                    else:
                                        trend = "remained stable"
                                    
                                    print(f"Merchant sentiment has {trend} over the course of the conversation.")
                                    print(f"Starting sentiment: {first_sentiment['category']} (score: {first_sentiment['score']:.2f})")
                                    print(f"Ending sentiment: {last_sentiment['category']} (score: {last_sentiment['score']:.2f})")
                                    
                                    # Generate sentiment trend visualization
                                    plot_sentiment_trend(sentiment_timeline)
                                    print("\nSentiment trend visualization has been saved as 'sentiment_trend.png'")
                                    
                                    # Detailed sentiment timeline
                                    print("\nDetailed Sentiment Timeline:")
                                    for entry in sentiment_timeline:
                                        print(f"\nDate: {entry['date'].strftime('%Y-%m-%d %H:%M:%S')}")
                                        print(f"Sentiment: {entry['category']} (score: {entry['score']:.2f})")
                                        if entry['details']:
                                            print(f"Emotions: {entry['details']['emotions']}")
                                            print(f"Explanation: {entry['details']['explanation']}")
                            else:
                                print("\nNo merchant emails found for sentiment analysis.")
                        else:
                            print(f"No emails found for case number: {case_number} (ID: {case_id})")
                    else:
                        print(f"Could not find case ID in the response for case number: {case_number}")
                else:
                    print(f"No case found with the given case number: {case_number}")
                    
            except Exception as e:
                print(f"Error occurred while processing case number {case_number}: {e}")
                if isinstance(e, grpc.RpcError):
                    print(f"Status code: {e.code()}")
                    print(f"Details: {e.details()}")
        else:
            parser.print_help()

if __name__ == "__main__":
    main() 