from flask import Flask, render_template, request, jsonify
import os
import sys
import json

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import the coo_audit module and Salesforce client
from coo_audit import process_emails
from salesforce.client import get_salesforce_client

app = Flask(__name__)

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