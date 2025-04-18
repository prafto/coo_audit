#!/usr/bin/env python3
"""
COO Service Client

This script provides a command-line interface to interact with the Change of Ownership
Onboarding service via gRPC. It allows retrieving store COO data by store ID.
"""

import os
import sys
import argparse
import logging
from datetime import datetime
from dotenv import load_dotenv
import grpc
from google.protobuf import wrappers_pb2

# Add the generated code directory to Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'protos', 'generated'))

# Import the generated protobuf code
from onboarding_service import change_of_ownership_onboarding_pb2 as protobufx
from onboarding_service import change_of_ownership_onboarding_pb2_grpc as change_of_ownership_grpc

# Status mappings
APPROVAL_STATUS_MAP = {
    0: "PENDING",
    1: "APPROVED",
    2: "REJECTED",
    3: "CANCELLED"
}

ONBOARDING_STATUS_MAP = {
    0: "NOT_STARTED",
    1: "IN_PROGRESS",
    2: "COMPLETED",
    3: "FAILED",
    4: "CANCELLED"
}

COO_STATUS_MAP = {
    "COO_STATUS_COMPLETE": "Completed",
    "COO_STATUS_INITIATED": "Initiated",
    "COO_STATUS_CANCELLED": "Cancelled",
    "COO_STATUS_FAILED": "Failed",
    "COO_STATUS_IN_PROGRESS": "In Progress"
}

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Load environment variables
env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
logger.info(f"Loading environment variables from: {env_path}")
load_dotenv(env_path)

# Get service credentials from environment variables
ONBOARDING_SERVICE_API_KEY = os.getenv('ONBOARDING_SERVICE_API_KEY')
ONBOARDING_SERVICE_WEB_SERVICE_URL = os.getenv('ONBOARDING_SERVICE_WEB_SERVICE_URL')

logger.info(f"ONBOARDING_SERVICE_API_KEY: {'*' * len(ONBOARDING_SERVICE_API_KEY) if ONBOARDING_SERVICE_API_KEY else 'None'}")
logger.info(f"ONBOARDING_SERVICE_WEB_SERVICE_URL: {ONBOARDING_SERVICE_WEB_SERVICE_URL}")

if not ONBOARDING_SERVICE_API_KEY or not ONBOARDING_SERVICE_WEB_SERVICE_URL:
    logger.error("Missing required environment variables. Please check your .env file.")
    sys.exit(1)

class OnboardingServiceClient:
    channel = None
    stub = None

    @staticmethod
    def get_headers():
        """Get the headers for authentication."""
        return [
            ("x-api-key", ONBOARDING_SERVICE_API_KEY),
            ("dd-api-secret", ONBOARDING_SERVICE_API_KEY),
            ("authority", "onboarding-service.doordash.com")
        ]

    @staticmethod
    def get_stub():
        """Get or create the gRPC stub."""
        if OnboardingServiceClient.channel is None or OnboardingServiceClient.stub is None:
            logger.info(f"Connecting to service at: {ONBOARDING_SERVICE_WEB_SERVICE_URL}")
            
            # Use basic insecure channel for development/testing
            OnboardingServiceClient.channel = grpc.insecure_channel(
                target=ONBOARDING_SERVICE_WEB_SERVICE_URL,
                options=[
                    ('grpc.enable_http_proxy', 0),
                    ('grpc.max_receive_message_length', 100 * 1024 * 1024),  # 100MB
                ]
            )
            
            logger.info("Channel created, creating stub...")
            OnboardingServiceClient.stub = change_of_ownership_grpc.ChangeOfOwnershipOnboardingServiceStub(
                OnboardingServiceClient.channel
            )
            logger.info("Stub created successfully")
            
        return OnboardingServiceClient.stub

    @staticmethod
    def get_store_change_of_ownership_onboarding(store_id: int):
        """Get COO data for a store ID."""
        stub = OnboardingServiceClient.get_stub()
        logger.info(f"Making request for store_id: {store_id}")
        headers = OnboardingServiceClient.get_headers()
        try:
            response = stub.GetStoreChangeOfOwnershipOnboarding(
                request=protobufx.GetStoreChangeOfOwnershipOnboardingRequest(
                    include_completed=wrappers_pb2.BoolValue(value=True),
                    store_id=wrappers_pb2.StringValue(value=str(store_id)),
                ),
                metadata=headers,
            )
            logger.info("Response received successfully")
            
            # Convert response to a dictionary with formatted values
            if response and response.store_change_of_ownership_onboarding:
                coo_data = response.store_change_of_ownership_onboarding
                formatted_data = {
                    'onboarding_id': coo_data.onboarding_id.value if coo_data.onboarding_id else None,
                    'business_id': coo_data.business_id.value if coo_data.business_id else None,
                    'legal_business_name': coo_data.legal_business_name.value if coo_data.legal_business_name else None,
                    'store_id': coo_data.store_id.value if coo_data.store_id else None,
                    'store_name': coo_data.store_name.value if coo_data.store_name else None,
                    'scheduled_cutoff_time': format_timestamp(coo_data.scheduled_cutoff_time),
                    'new_owner_first_name': coo_data.new_owner_first_name.value if coo_data.new_owner_first_name else None,
                    'new_owner_last_name': coo_data.new_owner_last_name.value if coo_data.new_owner_last_name else None,
                    'new_owner_email': coo_data.new_owner_email.value if coo_data.new_owner_email else None,
                    'new_owner_phone': coo_data.new_owner_phone.value if coo_data.new_owner_phone else None,
                    'requester_user_id': coo_data.requester_user_id.value if coo_data.requester_user_id else None,
                    'new_user_id': coo_data.new_user_id.value if coo_data.new_user_id else None,
                    'old_user_id': coo_data.old_user_id.value if coo_data.old_user_id else None,
                    'revoke_access': coo_data.revoke_access.value if coo_data.revoke_access else None,
                    'create_new_business': coo_data.create_new_business.value if coo_data.create_new_business else None,
                    'approved_at': format_timestamp(coo_data.approved_at),
                    'approval_status': APPROVAL_STATUS_MAP.get(int(coo_data.approval_status), f"UNKNOWN ({coo_data.approval_status})"),
                    'onboarding_status': ONBOARDING_STATUS_MAP.get(int(coo_data.onboarding_status), f"UNKNOWN ({coo_data.onboarding_status})"),
                    'payment_account_id': coo_data.payment_account_id.value if coo_data.payment_account_id else None,
                    'pactsafe_activity_id': coo_data.pactsafe_activity_id.value if coo_data.pactsafe_activity_id else None,
                    'batch_request_id': coo_data.batch_request_id.value if coo_data.batch_request_id else None,
                    'cancelled_at': format_timestamp(coo_data.cancelled_at),
                    'created_at': format_timestamp(coo_data.created_at),
                    'events': [format_event(str(event)) for event in coo_data.events] if coo_data.events else []
                }
                return formatted_data
            
            return None
        except Exception as e:
            logger.error(f"Error in gRPC call: {str(e)}")
            raise

def format_timestamp(timestamp):
    """Format a protobuf timestamp as a readable string."""
    if not timestamp or not timestamp.seconds:
        return "N/A"
    
    dt = datetime.fromtimestamp(timestamp.seconds)
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def format_event(event_str):
    """Format a COO event string to be more readable."""
    try:
        # Extract the status from the event string (format: "coo_status: COO_STATUS_COMPLETE ...")
        status = event_str.split("coo_status:")[1].strip().split()[0]
        # Get the human-readable status
        return COO_STATUS_MAP.get(status, status)
    except:
        return event_str

def print_coo_data(coo_data):
    """Print the COO data in a readable format."""
    if not coo_data:
        print("No COO data found.")
        return
    
    print("\n=== Store Change of Ownership Data ===")
    print(f"Onboarding ID: {coo_data['onboarding_id']}")
    print(f"Business ID: {coo_data['business_id']}")
    print(f"Legal Business Name: {coo_data['legal_business_name']}")
    print(f"Store ID: {coo_data['store_id']}")
    print(f"Store Name: {coo_data['store_name']}")
    print(f"Scheduled Cutoff Time: {coo_data['scheduled_cutoff_time']}")
    
    print("\n=== New Owner Information ===")
    print(f"Name: {coo_data['new_owner_first_name']} {coo_data['new_owner_last_name']}")
    print(f"Email: {coo_data['new_owner_email']}")
    print(f"Phone: {coo_data['new_owner_phone']}")
    
    print("\n=== User Information ===")
    print(f"Requester User ID: {coo_data['requester_user_id']}")
    print(f"New User ID: {coo_data['new_user_id']}")
    print(f"Old User ID: {coo_data['old_user_id']}")
    
    print("\n=== Status Information ===")
    print(f"Revoke Access: {coo_data['revoke_access']}")
    print(f"Create New Business: {coo_data['create_new_business']}")
    print(f"Approved At: {coo_data['approved_at']}")
    print(f"Approval Status: {coo_data['approval_status']}")
    print(f"Onboarding Status: {coo_data['onboarding_status']}")
    
    print("\n=== Additional Information ===")
    print(f"Payment Account ID: {coo_data['payment_account_id']}")
    print(f"Pactsafe Activity ID: {coo_data['pactsafe_activity_id']}")
    print(f"Batch Request ID: {coo_data['batch_request_id']}")
    print(f"Cancelled At: {coo_data['cancelled_at']}")
    print(f"Created At: {coo_data['created_at']}")
    
    # Print events if available
    if coo_data['events']:
        print("\n=== Events ===")
        for i, event in enumerate(coo_data['events'], 1):
            print(f"Event {i}: {event}")

def main():
    """Main function to parse arguments and execute the COO lookup."""
    parser = argparse.ArgumentParser(description='Retrieve Change of Ownership data for a store')
    parser.add_argument('store_id', help='The store ID to look up')
    parser.add_argument('--include-completed', action='store_true', help='Include completed COO records')
    
    args = parser.parse_args()
    
    try:
        # Get COO data
        coo_data = OnboardingServiceClient.get_store_change_of_ownership_onboarding(int(args.store_id))
        
        # Print the results
        if coo_data:
            print_coo_data(coo_data)
        else:
            print("No COO data found.")
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        sys.exit(1)
    finally:
        # Close the channel
        if OnboardingServiceClient.channel:
            OnboardingServiceClient.channel.close()

if __name__ == "__main__":
    main() 