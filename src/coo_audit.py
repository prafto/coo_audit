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
    max_length = 500  # Reduced from 512 to be safe
    
    try:
        # Get sentiment analysis with explicit truncation
        sentiment_result = sentiment_analyzer(
            clean_text, 
            truncation=True, 
            max_length=max_length,
            padding=True
        )[0]
        
        sentiment_label = sentiment_result['label']
        sentiment_score = sentiment_result['score']
        
        # Convert sentiment to our scale (-1 to 1)
        if sentiment_label == 'NEGATIVE':
            normalized_score = -sentiment_score
        else:  # POSITIVE
            normalized_score = sentiment_score
        
        # Get emotion analysis with explicit truncation
        emotion_result = emotion_analyzer(
            clean_text, 
            truncation=True, 
            max_length=max_length,
            padding=True
        )[0]
        
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
    
    # Set the backend to non-interactive to avoid GUI issues
    import matplotlib
    matplotlib.use('Agg')  # Use the 'Agg' backend which doesn't require a GUI
    
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

def get_salesforce_client():
    """Create and return a Salesforce client with the necessary configuration."""
    # Create metadata credentials
    api_secret = 'KGCu_nYudn_hdhjNn5UDRO2pnSX7kkjgS88cOCZ62j2R2X8My4eI9Brb3dS0E2MNu5OD_MzXyXAbceYsBiWPmDK7ksrq2S5eFwR2obebzu1zgiD19kM5f1gBG6Dh7Ehwd_OdIhssGcfNV_m9LkGUBXVeijUkQAdzASPl4pB-dGY'
    
    # Create channel options
    channel_options = [
        ('grpc.max_receive_message_length', 100 * 1024 * 1024),  # 100MB
    ]
    
    # Create a client instance with insecure connection
    return SalesforceClient(
        host="localhost",
        port=50051,
        use_ssl=False,
        channel_options=channel_options
    ), [('dd-api-secret', api_secret)]

def get_case_id_from_case_number(client, metadata, case_number):
    """Get the case ID from a case number using the Salesforce API."""
    try:
        # Create the request with the case number
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
            
            return case_id
        else:
            print(f"No case found with the given case number: {case_number}")
            return None
    except Exception as e:
        print(f"Error getting case ID for case number {case_number}: {e}")
        if isinstance(e, grpc.RpcError):
            print(f"Status code: {e.code()}")
            print(f"Details: {e.details()}")
        return None

def get_emails_for_case_id(client, metadata, case_id):
    """Get emails for a case ID using the Salesforce API."""
    try:
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
        
        return email_response.emails
    except Exception as e:
        print(f"Error getting emails for case ID {case_id}: {e}")
        if isinstance(e, grpc.RpcError):
            print(f"Status code: {e.code()}")
            print(f"Details: {e.details()}")
        return []

def process_emails(emails):
    """Process emails and extract relevant information."""
    processed_emails = []
    support_emails = 0
    merchant_emails = 0
    merchant_texts = []
    sentiment_timeline = []
    
    for email in emails:
        # Extract email details
        from_email = None
        from_address = None
        text_body = None
        email_date = None
        subject = None
        status = None
        
        for field in email.DESCRIPTOR.fields:
            field_name = field.name
            # Skip fields that don't have presence information or are too noisy
            if field_name in ['attachments', 'html_body']:
                continue
            
            # For status, handle it separately
            if field_name == 'status':
                try:
                    status_value = getattr(email, field_name)
                    status = get_email_status_description(status_value)
                except Exception as e:
                    print(f"Error getting status: {e}")
                    status = "Unknown"
                continue
            
            # For other fields, check if they have presence information
            if hasattr(email, 'HasField') and email.HasField(field_name):
                field_value = getattr(email, field_name)
                if hasattr(field_value, 'value'):
                    value = field_value.value
                    
                    # Store email details
                    if field_name == 'from_email':
                        from_email = value
                    elif field_name == 'from_address':
                        from_address = value
                    elif field_name == 'text_body':
                        text_body = value
                    elif field_name == 'created_date':
                        email_date = value
                    elif field_name == 'subject':
                        subject = value
        
        # Use from_address if available, otherwise fall back to from_email
        sender_address = from_address if from_address else from_email
        
        # Determine if it's a support or merchant email
        is_support = False
        if sender_address and sender_address.strip().lower() == "support@doordash.com":
            is_support = True
            support_emails += 1
        else:
            merchant_emails += 1
        
        # Process sentiment for merchant emails
        sentiment_score = 0
        sentiment_category = "Neutral"
        sentiment_details = None
        noteworthy_snippets = []
        
        if not is_support and text_body and text_body.strip():
            sentiment_score, sentiment_category, sentiment_details = analyze_sentiment_with_free_llm(text_body, email_date)
            merchant_texts.append(text_body)
            noteworthy_snippets = extract_noteworthy_snippets(text_body, sentiment_score)
            
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
                except Exception as e:
                    print(f"Error parsing date {email_date}: {e}")
        
        # Add email details to the list
        processed_emails.append({
            'from': sender_address,
            'date': email_date,
            'subject': subject,
            'body': text_body,
            'status': status,
            'is_support': is_support,
            'sentiment_score': sentiment_score,
            'sentiment_category': sentiment_category,
            'noteworthy_snippets': noteworthy_snippets
        })
    
    # Sort sentiment timeline by date
    sentiment_timeline.sort(key=lambda x: x['date'])
    
    return {
        'emails': processed_emails,
        'support_emails': support_emails,
        'merchant_emails': merchant_emails,
        'merchant_texts': merchant_texts,
        'sentiment_timeline': sentiment_timeline
    }

def extract_noteworthy_snippets(text, sentiment_score):
    """Extract noteworthy snippets from the email text based on sentiment."""
    if not text:
        return []
    
    # Clean the text
    clean_text = re.sub(r'<[^>]+>', '', text)
    
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', clean_text)
    
    # Filter sentences based on sentiment
    if sentiment_score < -0.5:
        # For negative sentiment, look for sentences with negative words
        negative_words = ['angry', 'frustrated', 'unhappy', 'disappointed', 'terrible', 'bad', 'worst', 'horrible', 'upset', 'annoyed']
        return [s for s in sentences if any(word in s.lower() for word in negative_words)]
    elif sentiment_score > 0.5:
        # For positive sentiment, look for sentences with positive words
        positive_words = ['happy', 'pleased', 'thank', 'great', 'excellent', 'good', 'wonderful', 'amazing', 'appreciate', 'satisfied']
        return [s for s in sentences if any(word in s.lower() for word in positive_words)]
    else:
        # For neutral sentiment, return a few sentences from the middle
        return sentences[:3] if len(sentences) > 3 else sentences

def get_case_emails(case_number):
    """
    Retrieve emails for a given case number using the Salesforce API.
    This function is used by the web application.
    
    Args:
        case_number: The case number to look up emails for
        
    Returns:
        A list of processed email objects with sentiment analysis
    """
    try:
        # Get Salesforce client
        client, metadata = get_salesforce_client()
        
        # Get emails for the case number
        with client as sf_client:
            # First, get the case ID from the case number
            case_id = get_case_id_from_case_number(sf_client, metadata, case_number)
            
            if not case_id:
                print(f"No case found with the given case number: {case_number}")
                return []
            
            # Then get emails for the case ID
            emails = get_emails_for_case_id(sf_client, metadata, case_id)
            
            if not emails:
                print(f"No emails found for case number: {case_number} (ID: {case_id})")
                return []
            
            # Process the emails
            result = process_emails(emails)
            return result['emails']
    
    except Exception as e:
        print(f"Error in get_case_emails: {e}")
        return []

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
    
    # Get Salesforce client
    client, metadata = get_salesforce_client()
    
    with client as sf_client:
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
                case_response = sf_client.stub.GetSalesforceCasesByCaseNumber(
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
            
            try:
                # Get the case ID from the case number
                case_id = get_case_id_from_case_number(sf_client, metadata, case_number)
                
                if case_id:
                    print(f"Found case ID: {case_id}")
                    
                    # Now fetch the emails using the case ID
                    print("\n" + "="*50)
                    print(f"Fetching emails for case ID: {case_id}")
                    print("="*50)
                    
                    # Get emails for the case ID
                    emails = get_emails_for_case_id(sf_client, metadata, case_id)
                    
                    # Process and display email data
                    if emails:
                        print(f"\nFound {len(emails)} emails for case number: {case_number} (ID: {case_id})")
                        
                        # Process the emails
                        result = process_emails(emails)
                        processed_emails = result['emails']
                        support_emails = result['support_emails']
                        merchant_emails = result['merchant_emails']
                        merchant_texts = result['merchant_texts']
                        sentiment_timeline = result['sentiment_timeline']
                        
                        # Print email details
                        for i, email in enumerate(processed_emails, 1):
                            print(f"\nEmail #{i}:")
                            print(f"From: {email['from']}")
                            print(f"Date: {email['date']}")
                            print(f"Subject: {email['subject']}")
                            print(f"Status: {email['status']}")
                            
                            if not email['is_support']:
                                print(f"Sentiment: {email['sentiment_category']} (score: {email['sentiment_score']:.2f})")
                                if email['noteworthy_snippets']:
                                    print("Noteworthy snippets:")
                                    for snippet in email['noteworthy_snippets']:
                                        print(f"  - {snippet}")
                        
                        # Print summary section
                        print("\n" + "="*50)
                        print("EMAIL SUMMARY")
                        print("="*50)
                        
                        # Email statistics
                        print(f"\nEmail Statistics:")
                        print(f"Total Emails: {len(processed_emails)}")
                        print(f"Support Emails: {support_emails}")
                        print(f"Merchant Emails: {merchant_emails}")
                        
                        # Sentiment analysis
                        if merchant_texts:
                            print(f"\nMerchant Sentiment Analysis:")
                            
                            # Calculate sentiment categories
                            sentiment_categories = [email['sentiment_category'] for email in processed_emails if not email['is_support']]
                            sentiment_counts = Counter(sentiment_categories)
                            total_sentiments = len(sentiment_categories)
                            
                            for sentiment, count in sentiment_counts.items():
                                percentage = (count / total_sentiments) * 100
                                print(f"{sentiment}: {count} emails ({percentage:.1f}%)")
                            
                            # Overall sentiment
                            most_common_sentiment = sentiment_counts.most_common(1)[0][0]
                            print(f"\nOverall Merchant Sentiment: {most_common_sentiment}")
                            
                            # Calculate average sentiment score
                            sentiment_scores = [email['sentiment_score'] for email in processed_emails if not email['is_support']]
                            avg_score = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
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
                    
            except Exception as e:
                print(f"Error occurred while processing case number {case_number}: {e}")
                if isinstance(e, grpc.RpcError):
                    print(f"Status code: {e.code()}")
                    print(f"Details: {e.details()}")
        else:
            parser.print_help()

if __name__ == "__main__":
    main() 