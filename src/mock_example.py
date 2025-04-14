import grpc
from google.protobuf import wrappers_pb2

class MockSalesforceResponse:
    """Mock response object that mimics the structure of the actual response."""
    def __init__(self, case_ids):
        self.next_page_token = "mock_token"
        self.case_details = [MockCaseDetail(case_id) for case_id in case_ids]

class MockCaseDetail:
    """Mock case detail object."""
    def __init__(self, case_id):
        self.salesforce_case_id = case_id
        self.history_items = ["history1", "history2"]
        self.feed_items = ["feed1", "feed2"]
        self.emails = ["email1", "email2"]
        self.contact_trace_records = ["trace1", "trace2"]

class MockSalesforceClient:
    """Mock client that mimics the behavior of the actual client."""
    def __init__(self, host, port, use_ssl=False):
        self.host = host
        self.port = port
        self.use_ssl = use_ssl
        self.channel = grpc.insecure_channel(f"{host}:{port}")
    
    def get_salesforce_case_details(self, case_ids, page_size=100, start_time=None, end_time=None):
        """Mock implementation of get_salesforce_case_details."""
        return MockSalesforceResponse(case_ids)
    
    def close(self):
        self.channel.close()
    
    def __enter__(self):
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

def main():
    # Example case IDs
    case_ids = ["5001234567", "5001234568"]
    
    # Create a mock client instance
    with MockSalesforceClient(
        host="localhost",
        port=50051,
        use_ssl=False
    ) as client:
        try:
            # Get case details using the mock client
            response = client.get_salesforce_case_details(
                case_ids=case_ids,
                page_size=10,
                start_time="2024-01-01T00:00:00Z",
                end_time="2024-03-21T23:59:59Z"
            )
            
            # Print the response details
            print("Received response:")
            print(f"Next page token: {response.next_page_token}")
            
            # Print case details
            for case in response.case_details:
                print(f"\nCase ID: {case.salesforce_case_id}")
                print(f"Number of history items: {len(case.history_items)}")
                print(f"Number of feed items: {len(case.feed_items)}")
                print(f"Number of emails: {len(case.emails)}")
                print(f"Number of contact trace records: {len(case.contact_trace_records)}")
                
        except Exception as e:
            print(f"Error occurred: {e}")

if __name__ == "__main__":
    main() 