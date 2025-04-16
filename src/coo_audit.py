from salesforce.client import SalesforceClient, get_salesforce_client
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

def analyze_sentiment(text):
    """Analyze the sentiment of a text using the sentiment analyzer."""
    try:
        # Load models if not already loaded
        load_models()
        
        # Analyze sentiment
        sentiment_result = sentiment_analyzer(text)[0]
        sentiment_score = sentiment_result['score']
        sentiment_label = sentiment_result['label']
        
        # Analyze emotions
        emotion_result = emotion_analyzer(text)[0]
        emotions = emotion_result['label']
        
        # Determine sentiment category
        if sentiment_label == 'POSITIVE':
            category = 'Positive'
        elif sentiment_label == 'NEGATIVE':
            category = 'Negative'
        else:
            category = 'Neutral'
        
        # Generate explanation
        explanation = f"The text has a {category.lower()} sentiment with a score of {sentiment_score:.2f}. The emotions detected are: {emotions}."
        
        return sentiment_score, category, {
            "emotions": emotions,
            "explanation": explanation
        }
        
    except Exception as e:
        print(f"Error in sentiment analysis: {e}")
        return 0, "Neutral", None

def process_emails(emails):
    """Process emails and extract relevant information."""
    processed_emails = []
    support_emails = 0
    merchant_emails = 0
    merchant_texts = []
    sentiment_timeline = []
    
    print(f"\nProcessing {len(emails)} raw emails...")
    
    if not emails:
        print("No emails to process!")
        return {
            'emails': processed_emails,
            'support_emails': support_emails,
            'merchant_emails': merchant_emails,
            'merchant_texts': merchant_texts,
            'sentiment_timeline': sentiment_timeline
        }
    
    for i, email in enumerate(emails):
        print(f"\nProcessing email {i+1} of {len(emails)}")
        
        # Extract email details
        from_email = None
        from_address = None
        text_body = None
        email_date = None
        subject = None
        status = "Unknown"  # Default status
        
        print("Email fields:")
        for field in email.DESCRIPTOR.fields:
            field_name = field.name
            try:
                # Skip fields that don't have presence information or are too noisy
                if field_name in ['attachments', 'html_body', 'status']:  # Skip problematic fields
                    print(f"Skipping field: {field_name}")
                    continue
                
                # For other fields, check if they have presence information
                if hasattr(email, 'HasField') and email.HasField(field_name):
                    field_value = getattr(email, field_name)
                    if hasattr(field_value, 'value'):
                        value = field_value.value
                        print(f"{field_name}: {value}")
                        
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
                else:
                    print(f"Field {field_name} does not have presence information")
            except Exception as e:
                print(f"Error processing field {field_name}: {e}")
                continue
        
        # Skip emails without text body (we need this for sentiment analysis)
        if not text_body:
            print(f"Skipping email due to missing text body")
            continue
            
        # Use current time if email_date is missing
        if not email_date:
            email_date = datetime.now().isoformat()
            print(f"Using current time as email date: {email_date}")
        
        # Determine if it's a support email - use from_address or from_email
        is_support = False
        if from_address and 'support@doordash.com' in from_address.lower():
            is_support = True
        elif from_email and 'support@doordash.com' in from_email.lower():
            is_support = True
            
        print(f"Email classification: {'Support' if is_support else 'Merchant'} email")
        
        # Process the email
        processed_email = {
            'from': from_email,
            'from_address': from_address,
            'date': email_date,
            'subject': subject,
            'status': status,
            'is_support': is_support,
            'text': text_body
        }
        
        # Update counters
        if is_support:
            support_emails += 1
        else:
            merchant_emails += 1
            merchant_texts.append(text_body)
            
            # Analyze sentiment for merchant emails
            sentiment_score, sentiment_category, details = analyze_sentiment(text_body)
            
            # Add sentiment information to the processed email
            processed_email['sentiment_score'] = sentiment_score
            processed_email['sentiment_category'] = sentiment_category
            processed_email['noteworthy_snippets'] = []
            
            # Add to sentiment timeline - store email_date as is (string)
            sentiment_timeline.append({
                'date': email_date,  # Keep as string, don't convert to datetime
                'score': sentiment_score,
                'category': sentiment_category,
                'details': details
            })
        
        processed_emails.append(processed_email)
        print(f"Successfully processed email {i+1}")
    
    print(f"\nProcessing complete:")
    print(f"Total processed emails: {len(processed_emails)}")
    print(f"Support emails: {support_emails}")
    print(f"Merchant emails: {merchant_emails}")
    
    return {
        'emails': processed_emails,
        'support_emails': support_emails,
        'merchant_emails': merchant_emails,
        'merchant_texts': merchant_texts,
        'sentiment_timeline': sentiment_timeline
    }

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
                            print(f"{field_name}: {field_value}")
                else:
                    print(f"No case found with the given case number: {case_number}")
                    
            except Exception as e:
                print(f"Error occurred while processing case number {case_number}: {e}")
                if isinstance(e, grpc.RpcError):
                    print(f"Status code: {e.code()}")
                    print(f"Details: {e.details()}")
                    
        elif args.command == 'audit_emails':
            # Email audit functionality
            case_number = args.case_number
            
            print(f"Looking up case ID for case number: {case_number}")
            print("="*50)
            
            try:
                # Get the case ID from the case number
                case_id = sf_client.get_case_id_from_case_number(metadata, case_number)
                
                if case_id:
                    print(f"Found case ID: {case_id}")
                    
                    # Now fetch the emails using the case ID
                    print("\n" + "="*50)
                    print(f"Fetching emails for case ID: {case_id}")
                    print("="*50)
                    
                    # Get emails for the case ID
                    emails = sf_client.get_emails_for_case_id(metadata, case_id)
                    
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
                        print(f"\nTotal Emails: {len(processed_emails)}")
                        print(f"Support Emails: {support_emails}")
                        print(f"Merchant Emails: {merchant_emails}")
                        
                        # Sentiment analysis summary
                        if merchant_emails > 0:
                            print("\nSENTIMENT ANALYSIS")
                            print("="*50)
                            
                            # Calculate average sentiment
                            sentiment_scores = [email['sentiment_score'] for email in processed_emails if not email['is_support']]
                            avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
                            
                            print(f"\nAverage Sentiment Score: {avg_sentiment:.2f}")
                            
                            # Sentiment distribution
                            sentiment_categories = [email['sentiment_category'] for email in processed_emails if not email['is_support']]
                            sentiment_counts = Counter(sentiment_categories)
                            
                            print("\nSentiment Distribution:")
                            for category, count in sentiment_counts.items():
                                percentage = (count / merchant_emails) * 100
                                print(f"{category}: {count} emails ({percentage:.1f}%)")
                            
                            # Detailed sentiment timeline
                            print("\nDetailed Sentiment Timeline:")
                            for entry in sentiment_timeline:
                                print(f"\nDate: {entry['date']}")  # Already a string, no need for strftime
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