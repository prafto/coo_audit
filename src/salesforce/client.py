"""
Salesforce gRPC client implementation for interacting with the SalesforceGatewayService.
"""
import grpc
from typing import List, Optional, Tuple
from datetime import datetime
from google.protobuf import wrappers_pb2, timestamp_pb2
from case_management_service.salesforce import salesforce_pb2
from case_management_service.salesforce import salesforce_pb2_grpc
from case_management_service import common_pb2
from common import money_pb2


def _str_to_timestamp(time_str: str) -> timestamp_pb2.Timestamp:
    """Convert ISO format time string to Timestamp."""
    dt = datetime.fromisoformat(time_str.replace('Z', '+00:00'))
    ts = timestamp_pb2.Timestamp()
    ts.FromDatetime(dt)
    return ts


def get_salesforce_client() -> Tuple['SalesforceClient', List[Tuple[str, str]]]:
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


class SalesforceClient:
    """Client for interacting with the Salesforce gRPC service."""

    def __init__(
        self,
        host: str = "localhost",
        port: int = 50051,
        use_ssl: bool = False,
        ssl_credentials: Optional[grpc.ChannelCredentials] = None,
        channel_options: Optional[List[tuple]] = None,
    ):
        self.host = host
        self.port = port
        self.use_ssl = use_ssl
        self.ssl_credentials = ssl_credentials
        self.channel_options = channel_options or []
        self.channel = None
        self.stub = None

    def __enter__(self):
        target = f"{self.host}:{self.port}"
        
        # Default channel options if none provided
        if not self.channel_options:
            self.channel_options = [
                ('grpc.ssl_target_name_override', self.host),
                ('grpc.default_authority', self.host),
                ('grpc.max_receive_message_length', 100 * 1024 * 1024),  # 100MB
            ]
        
        if self.use_ssl:
            if self.ssl_credentials is None:
                self.ssl_credentials = grpc.ssl_channel_credentials()
            self.channel = grpc.secure_channel(
                target,
                self.ssl_credentials,
                options=self.channel_options
            )
        else:
            self.channel = grpc.insecure_channel(
                target,
                options=self.channel_options
            )
        
        self.stub = salesforce_pb2_grpc.SalesforceGatewayServiceStub(self.channel)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.channel:
            self.channel.close()

    def get_case_id_from_case_number(self, metadata: List[Tuple[str, str]], case_number: str) -> Optional[str]:
        """Get the case ID from a case number using the Salesforce API."""
        try:
            # Create the request with the case number
            case_request = salesforce_pb2.GetSalesforceCasesByCaseNumberRequest(
                case_number=wrappers_pb2.StringValue(value=case_number)
            )
            
            # Make the call to get case details
            case_response = self.stub.GetSalesforceCasesByCaseNumber(
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

    def get_emails_for_case_id(self, metadata: List[Tuple[str, str]], case_id: str) -> List[salesforce_pb2.SalesforceEmail]:
        """Get emails for a case ID using the Salesforce API."""
        try:
            print(f"\nFetching emails for case ID: {case_id}")
            
            # Create the request with the case ID
            email_request = salesforce_pb2.GetSalesforceEmailsRequest(
                salesforce_case_ids=[wrappers_pb2.StringValue(value=case_id)]
            )
            
            print(f"Request created: {email_request}")
            
            # Make the call to get emails
            print("Making gRPC call to GetSalesforceEmails...")
            email_response = self.stub.GetSalesforceEmails(
                email_request,
                metadata=metadata,
                timeout=30.0
            )
            
            print(f"Response received: {email_response}")
            print(f"Retrieved {len(email_response.emails)} emails from Salesforce")
            
            # Log email details for debugging
            for i, email in enumerate(email_response.emails):
                print(f"\nEmail {i + 1}:")
                for field in email.DESCRIPTOR.fields:
                    try:
                        if hasattr(email, 'HasField') and email.HasField(field.name):
                            field_value = getattr(email, field.name)
                            if hasattr(field_value, 'value'):
                                print(f"{field.name}: {field_value.value}")
                    except Exception as e:
                        print(f"Error accessing field {field.name}: {e}")
            
            return email_response.emails
        except Exception as e:
            print(f"Error getting emails for case ID {case_id}: {e}")
            if isinstance(e, grpc.RpcError):
                print(f"Status code: {e.code()}")
                print(f"Details: {e.details()}")
            return []

    def get_salesforce_case_details(
        self,
        case_ids: List[wrappers_pb2.StringValue],
        page_size: int = 100,
        page_token: Optional[str] = None,
        start_time: Optional[str] = None,
        end_time: Optional[str] = None,
        timeout: Optional[float] = None,
    ) -> salesforce_pb2.GetSalesforceCaseDetailsResponse:
        """Get details for Salesforce cases including history, feed items, emails and contact trace records.
        
        Args:
            case_ids: List of Salesforce case IDs to get details for
            page_size: Number of items per page for pagination
            page_token: Token for pagination (not used, kept for backward compatibility)
            start_time: Start time filter in ISO format (optional)
            end_time: End time filter in ISO format (optional)
            timeout: RPC timeout in seconds (optional)
        
        Returns:
            GetSalesforceCaseDetailsResponse containing case history, feed items, emails and contact trace records
        
        Raises:
            grpc.RpcError: If the RPC call fails
        """
        # Create pagination options with offset and limit
        offset_pagination_options = common_pb2.OffsetPaginationOptions(
            offset=0,  # Start from the beginning
            limit=page_size
        )
        
        pagination_options = common_pb2.PaginationOptions(
            offset_paging_options=offset_pagination_options
        )

        # Create time filter options if provided
        time_filter_options = None
        if start_time and end_time:
            time_filter_options = common_pb2.TimeFilterOptions(
                created_after=_str_to_timestamp(start_time),
                created_before=_str_to_timestamp(end_time)
            )

        # Create the request message
        request = salesforce_pb2.GetSalesforceCaseDetailsRequest(
            salesforce_case_ids=case_ids,
            pagination_options=pagination_options,
            time_filter_options=time_filter_options
        )

        try:
            response = self.stub.GetSalesforceCaseDetails(
                request,
                timeout=timeout
            )
            return response
        except grpc.RpcError as e:
            # Log the error details
            status_code = e.code()
            details = e.details()
            print(f"RPC failed with status {status_code}: {details}")
            raise