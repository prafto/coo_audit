"""
Salesforce gRPC client implementation for interacting with the SalesforceGatewayService.
"""
import grpc
from typing import List, Optional
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

    def get_salesforce_cases_by_case_number(
        self,
        case_number: wrappers_pb2.StringValue,
        timeout: Optional[float] = None,
    ) -> salesforce_pb2.GetSalesforceCasesByCaseNumberResponse:
        """Get a Salesforce case by its case number.
        
        Args:
            case_number: The case number to look up
            timeout: RPC timeout in seconds (optional)
        
        Returns:
            GetSalesforceCasesByCaseNumberResponse containing the case details
        
        Raises:
            grpc.RpcError: If the RPC call fails
        """
        # Create the request message
        request = salesforce_pb2.GetSalesforceCasesByCaseNumberRequest(
            case_number=case_number
        )

        try:
            response = self.stub.GetSalesforceCasesByCaseNumber(
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