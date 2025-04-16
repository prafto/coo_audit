from flask import Flask, render_template, request, jsonify
import os
import sys
import json
import re
from datetime import datetime
from collections import Counter
from transformers import pipeline
import io
import base64
from io import BytesIO
import numpy as np

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import the coo_audit module and Salesforce client
from coo_audit import process_emails
from salesforce.client import get_salesforce_client

app = Flask(__name__)

# Initialize the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_sentiment(text):
    """Analyze sentiment using the Hugging Face model."""
    try:
        # Clean and prepare the text
        text = text.strip()
        if not text:
            return {
                'score': 0,
                'category': 'Neutral',
                'emotions': [],
                'explanation': 'No text provided for analysis'
            }
        
        # Get sentiment prediction
        result = sentiment_analyzer(text)[0]
        
        # Convert score to our scale (-1 to 1)
        score = result['score']
        if result['label'] == 'NEGATIVE':
            score = -score
        
        # Determine category
        if score > 0.3:
            category = 'Positive'
        elif score < -0.3:
            category = 'Negative'
        else:
            category = 'Neutral'
        
        return {
            'score': score,
            'category': category,
            'emotions': [],  # Hugging Face model doesn't provide emotions
            'explanation': f'Text analyzed as {category.lower()} with confidence {abs(score):.2f}'
        }
    except Exception as e:
        print(f"Error in sentiment analysis: {str(e)}")
        return {
            'score': 0,
            'category': 'Neutral',
            'emotions': [],
            'explanation': f'Error analyzing sentiment: {str(e)}'
        }

def get_sentiment_color(sentiment_score):
    """Convert sentiment score to a color gradient."""
    if sentiment_score > 0.6:
        return "#2ecc71"  # Bright green for very positive
    elif sentiment_score > 0.2:
        return "#27ae60"  # Green for positive
    elif sentiment_score > 0:
        return "#a8e6cf"  # Light green for slightly positive
    elif sentiment_score > -0.2:
        return "#d5f5e3"  # Very light green for neutral
    elif sentiment_score > -0.6:
        return "#fadbd8"  # Light red for slightly negative
    elif sentiment_score > -0.8:
        return "#f1948a"  # Red for negative
    else:
        return "#e74c3c"  # Bright red for very negative

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_case():
    """API endpoint to analyze a case and return the results."""
    try:
        # Get the case number from the request
        data = request.get_json()
        case_number = data.get('case_number')
        
        if not case_number:
            return jsonify({'error': 'Case number is required'}), 400
        
        # Get Salesforce client
        client, metadata = get_salesforce_client()
        
        # Get emails for the case
        with client as sf_client:
            # First, get the case ID from the case number
            case_id = sf_client.get_case_id_from_case_number(metadata, case_number)
            
            if not case_id:
                return jsonify({'error': f'No case found with the given case number: {case_number}'}), 404
            
            # Then get emails for the case ID
            emails = sf_client.get_emails_for_case_id(metadata, case_id)
            
            if not emails:
                return jsonify({'error': f'No emails found for case number: {case_number} (ID: {case_id})'}), 404
            
            # Process the emails
            result = process_emails(emails)
            processed_emails = result['emails']
            support_emails = result['support_emails']
            merchant_emails = result['merchant_emails']
            sentiment_timeline = result['sentiment_timeline']
        
        # Calculate average sentiment score
        sentiment_scores = [email.get('sentiment_score', 0) for email in processed_emails if not email.get('is_support', False)]
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
        
        # Return the results
        return jsonify({
            'emails': processed_emails,
            'total_emails': len(processed_emails),
            'support_emails': support_emails,
            'merchant_emails': merchant_emails,
            'avg_sentiment': avg_sentiment,
            'sentiment_timeline': [
                {
                    'date': item['date'],  # Date is already a string, no need for strftime
                    'score': item['score'],
                    'category': item['category']
                } for item in sentiment_timeline
            ]
        })
    
    except Exception as e:
        print(f"Error analyzing case: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 