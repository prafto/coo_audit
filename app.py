from flask import Flask, render_template, request, jsonify
import os
import sys
import json
from datetime import datetime

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import the coo_audit module and Salesforce client
from coo_audit import process_emails
from salesforce.client import get_salesforce_client
from coo_service import OnboardingServiceClient

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_case():
    """API endpoint to analyze a case and return the results."""
    try:
        # Get the case number and store ID from the request
        data = request.get_json()
        case_number = data.get('case_number')
        store_id = data.get('store_id')
        
        if not case_number or not store_id:
            return jsonify({'error': 'Both case number and store ID are required'}), 400
        
        # Get COO information
        coo_info = None
        try:
            # Get COO data
            coo_data = OnboardingServiceClient.get_store_change_of_ownership_onboarding(int(store_id))
            
            if coo_data:
                # Get the latest event for COO status
                latest_event = None
                if coo_data['events']:
                    latest_event = coo_data['events'][-1]

                coo_info = {
                    'store_id': store_id,
                    'store_name': coo_data['store_name'],
                    'new_owner_name': f"{coo_data['new_owner_first_name'] or ''} {coo_data['new_owner_last_name'] or ''}".strip(),
                    'new_owner_email': coo_data['new_owner_email'],
                    'coo_status': latest_event,
                    'approved_at': coo_data['approved_at'],
                    'approval_status': coo_data['approval_status'],
                    'onboarding_status': coo_data['onboarding_status']
                }
            
        except Exception as e:
            if "NOT_FOUND" in str(e):
                app.logger.info(f"No COO data found for store {store_id}")
                coo_info = None
            else:
                app.logger.error(f"Error fetching COO data: {str(e)}")
                coo_info = None
        
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
        
        # Filter to only include merchant emails for the frontend
        merchant_only_emails = [email for email in processed_emails if not email.get('is_support', False)]
        
        # Calculate average sentiment score
        sentiment_scores = [email.get('sentiment_score', 0) for email in merchant_only_emails]
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
        
        # Return the results
        return jsonify({
            'emails': merchant_only_emails,  # Only merchant emails
            'total_emails': len(processed_emails),  # Total count of all emails
            'support_emails': support_emails,
            'merchant_emails': merchant_emails,
            'avg_sentiment': avg_sentiment,
            'sentiment_timeline': [
                {
                    'date': item['date'],  # Date is already a string, no need for strftime
                    'score': item['score'],
                    'category': item['category']
                } for item in sentiment_timeline
            ],
            'coo_info': coo_info
        })
    
    except Exception as e:
        app.logger.error(f"Error analyzing case: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 