from flask import Flask, render_template, request, jsonify
import os
import sys
import json
import re
from datetime import datetime
from collections import Counter
from transformers import pipeline
import matplotlib
matplotlib.use('Agg')  # Set the backend to non-interactive before importing pyplot
import matplotlib.pyplot as plt
import io
import base64
from io import BytesIO
import numpy as np

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import the coo_audit module
from coo_audit import get_case_emails, plot_sentiment_trend

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

def generate_sentiment_trend_chart(sentiment_timeline):
    """Generate a sentiment trend chart and return as base64 encoded image."""
    if not sentiment_timeline:
        return None
    
    # Extract data for plotting
    dates = [item['date'] for item in sentiment_timeline]
    scores = [item['score'] for item in sentiment_timeline]
    
    # Create the plot
    plt.figure(figsize=(10, 4))
    
    # Plot sentiment scores with color gradient
    for i in range(len(dates) - 1):
        plt.plot([dates[i], dates[i+1]], [scores[i], scores[i+1]], 
                 color=get_sentiment_color((scores[i] + scores[i+1]) / 2),
                 linewidth=3)
    
    # Add points
    plt.scatter(dates, scores, color='black', s=50)
    
    # Customize the plot
    plt.title('Sentimento-Meter: Merchant Sentiment Over Time', fontsize=14)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Sentiment Score', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Set y-axis limits
    plt.ylim(-1.2, 1.2)
    
    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    
    # Add a horizontal line at y=0
    plt.axhline(y=0, color='black', linestyle='--', alpha=0.3)
    
    # Adjust layout
    plt.tight_layout()
    
    # Save the plot to a bytes buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.close()
    
    # Encode the image as base64
    img_str = base64.b64encode(buf.read()).decode('utf-8')
    return img_str

@app.route('/')
def index():
    """Render the main page of the COO Audit Tool."""
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
        
        # Get emails for the case
        emails = get_case_emails(case_number)
        
        if not emails:
            return jsonify({'error': f'No emails found for case number: {case_number}'}), 404
        
        # Count support vs merchant emails
        support_emails = sum(1 for email in emails if email.get('is_support', False))
        merchant_emails = sum(1 for email in emails if not email.get('is_support', False))
        
        # Extract email content for sentiment analysis
        merchant_texts = [email.get('body', '') for email in emails if not email.get('is_support', False)]
        
        # Build sentiment timeline
        sentiment_timeline = []
        for email in emails:
            if not email.get('is_support', False) and email.get('date') and email.get('sentiment_score') is not None:
                try:
                    date = datetime.fromisoformat(email['date'].replace('Z', '+00:00'))
                    sentiment_timeline.append({
                        'date': date,
                        'score': email.get('sentiment_score', 0),
                        'category': email.get('sentiment_category', 'Neutral')
                    })
                except Exception as e:
                    print(f"Error parsing date {email.get('date')}: {e}")
        
        # Sort sentiment timeline by date
        sentiment_timeline.sort(key=lambda x: x['date'])
        
        # Calculate average sentiment score
        sentiment_scores = [email.get('sentiment_score', 0) for email in emails if not email.get('is_support', False)]
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
        
        # Generate sentiment trend chart
        chart_path = None
        if sentiment_timeline:
            try:
                # Create the plot
                plt.figure(figsize=(10, 4))
                
                # Extract data for plotting
                dates = [item['date'] for item in sentiment_timeline]
                scores = [item['score'] for item in sentiment_timeline]
                categories = [item['category'] for item in sentiment_timeline]
                
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
                
                # Save the plot to a BytesIO object
                img = BytesIO()
                plt.savefig(img, format='png')
                img.seek(0)
                plt.close()
                
                # Convert to base64 for embedding in HTML
                chart_path = base64.b64encode(img.getvalue()).decode('utf-8')
            except Exception as e:
                print(f"Error generating chart: {e}")
        
        # Return the results
        return jsonify({
            'emails': emails,
            'total_emails': len(emails),
            'support_emails': support_emails,
            'merchant_emails': merchant_emails,
            'avg_sentiment': avg_sentiment,
            'sentiment_timeline': [
                {
                    'date': item['date'].strftime('%Y-%m-%d %H:%M:%S'),
                    'score': item['score'],
                    'category': item['category']
                } for item in sentiment_timeline
            ],
            'chart_path': chart_path
        })
    
    except Exception as e:
        print(f"Error analyzing case: {e}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 