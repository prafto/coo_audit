from salesforce.client import SalesforceClient
import grpc
import ssl
import argparse
from google.protobuf import wrappers_pb2
from case_management_service.salesforce import salesforce_pb2
from case_management_service.salesforce import salesforce_pb2_grpc
from case_management_service import common_pb2

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Get Salesforce case details by case number')
    parser.add_argument('case_number', help='The case number to look up')
    args = parser.parse_args()
    
    # Case number from command line argument
    case_number = args.case_number
    
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

if __name__ == "__main__":
    main() 