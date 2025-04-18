from flask import Flask, render_template, request, jsonify
import os
import sys
import json
import asyncio
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

# Import the coo_audit module and Salesforce client
from coo_audit import process_emails
from salesforce.client import get_salesforce_client
from coo_service import OnboardingServiceClient, format_timestamp, calculate_coo_duration

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
        
        logger.debug(f"Received request for case_number: {case_number}, store_id: {store_id}")
        
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
        
        # Filter to only include merchant emails for the frontend
        merchant_only_emails = [email for email in processed_emails if not email.get('is_support', False)]
        
        # Calculate average sentiment score
        sentiment_scores = [email.get('sentiment_score', 0) for email in merchant_only_emails]
        avg_sentiment = sum(sentiment_scores) / len(sentiment_scores) if sentiment_scores else 0
        
        # Get COO information if store_id is provided
        coo_data = {}
        if store_id:
            try:
                logger.debug(f"Fetching COO data for store_id: {store_id}")
                # Run the async function to get COO data
                loop = asyncio.new_event_loop()
                asyncio.set_event_loop(loop)
                response = loop.run_until_complete(
                    OnboardingServiceClient.get_store_change_of_ownership_onboarding(int(store_id))
                )
                loop.close()
                
                logger.debug(f"COO response received: {response}")
                
                if response and response.store_change_of_ownership_onboarding:
                    coo_record = response.store_change_of_ownership_onboarding
                    logger.debug(f"COO record found: {coo_record}")
                    
                    # Calculate COO process duration
                    start_time = None
                    end_time = None
                    
                    # Safely access timestamp fields
                    if hasattr(coo_record, 'process_started_at') and coo_record.process_started_at:
                        if hasattr(coo_record.process_started_at, 'seconds'):
                            start_time = datetime.fromtimestamp(coo_record.process_started_at.seconds)
                    
                    if hasattr(coo_record, 'process_ended_at') and coo_record.process_ended_at:
                        if hasattr(coo_record.process_ended_at, 'seconds'):
                            end_time = datetime.fromtimestamp(coo_record.process_ended_at.seconds)
                    
                    duration = calculate_coo_duration(start_time, end_time)
                    
                    logger.debug(f"COO duration calculated: {duration}")
                    
                    # Format COO data for display
                    def get_proto_value(value):
                        if hasattr(value, 'value'):
                            return value.value
                        return value

                    coo_data = {
                        'onboarding_id': get_proto_value(getattr(coo_record, 'onboarding_id', None)),
                        'business_id': get_proto_value(getattr(coo_record, 'business_id', None)),
                        'legal_business_name': get_proto_value(getattr(coo_record, 'legal_business_name', None)),
                        'store_id': get_proto_value(getattr(coo_record, 'store_id', None)),
                        'store_name': get_proto_value(getattr(coo_record, 'store_name', None)),
                        'scheduled_cutoff_time': format_timestamp(getattr(coo_record, 'scheduled_cutoff_time', None)),
                        'process_started_at': format_timestamp(getattr(coo_record, 'process_started_at', None)),
                        'process_ended_at': format_timestamp(getattr(coo_record, 'process_ended_at', None)),
                        'duration': f"{duration[0]} days, {duration[1]} hours, {duration[2]} minutes" if duration else 'N/A',
                        'new_owner_first_name': get_proto_value(getattr(coo_record, 'new_owner_first_name', None)),
                        'new_owner_last_name': get_proto_value(getattr(coo_record, 'new_owner_last_name', None)),
                        'new_owner_email': get_proto_value(getattr(coo_record, 'new_owner_email', None)),
                        'new_owner_phone': get_proto_value(getattr(coo_record, 'new_owner_phone', None)),
                        'requester_user_id': get_proto_value(getattr(coo_record, 'requester_user_id', None)),
                        'new_user_id': get_proto_value(getattr(coo_record, 'new_user_id', None)),
                        'old_user_id': get_proto_value(getattr(coo_record, 'old_user_id', None)),
                        'revoke_access': get_proto_value(getattr(coo_record, 'revoke_access', False)),
                        'create_new_business': get_proto_value(getattr(coo_record, 'create_new_business', False)),
                        'approved_at': format_timestamp(getattr(coo_record, 'approved_at', None)),
                        'approval_status': get_proto_value(getattr(coo_record, 'approval_status', None)),
                        'onboarding_status': get_proto_value(getattr(coo_record, 'onboarding_status', None)),
                        'payment_account_id': get_proto_value(getattr(coo_record, 'payment_account_id', None)),
                        'pactsafe_activity_id': get_proto_value(getattr(coo_record, 'pactsafe_activity_id', None)),
                        'batch_request_id': get_proto_value(getattr(coo_record, 'batch_request_id', None)),
                        'cancelled_at': format_timestamp(getattr(coo_record, 'cancelled_at', None)),
                        'created_at': format_timestamp(getattr(coo_record, 'created_at', None)),
                        'events': []
                    }
                    
                    logger.debug(f"Formatted COO data: {json.dumps(coo_data, indent=2)}")
                    
                    # Add events if available
                    if coo_record.events:
                        for event in coo_record.events:
                            event_time = format_timestamp(event.event_time) if hasattr(event, 'event_time') and event.event_time else "N/A"
                            event_type = event.coo_status if hasattr(event, 'coo_status') else "Unknown"
                            coo_data['events'].append({
                                'timestamp': event_time,
                                'description': f"{event_type} - {event_time}"
                            })
                else:
                    logger.warning(f"No COO data found for store_id: {store_id}")
            except Exception as e:
                logger.error(f"Error getting COO data: {e}", exc_info=True)
                coo_data['error'] = str(e)
        
        # Prepare the response
        response_data = {
            'processed_emails': merchant_only_emails,  # Only merchant emails
            'total_emails': len(processed_emails),  # Total count of all emails
            'support_emails': support_emails,
            'merchant_emails': merchant_emails,
            'average_sentiment_score': avg_sentiment,
            'sentiment_timeline': [
                {
                    'timestamp': item['date'],  # Date is already a string, no need for strftime
                    'sentiment_score': item['score'],
                    'category': item['category'],
                    'details': {
                        'explanation': item.get('explanation', '')
                    }
                } for item in sentiment_timeline
            ],
            'coo_data': coo_data  # Add COO data to the response
        }
        
        logger.debug(f"Sending response with COO data: {json.dumps(coo_data, indent=2)}")
        
        # Return the results
        return jsonify(response_data)
    
    except Exception as e:
        logger.error(f"Error analyzing case: {e}", exc_info=True)
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True) 