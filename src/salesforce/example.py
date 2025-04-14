"""
Example usage of the Salesforce gRPC client.
"""
from salesforce import SalesforceClient
import grpc
from datetime import datetime, timedelta


def main():
    # Example configuration
    host = "localhost"  # Replace with your actual server host
    port = 50051        # Replace with your actual server port
    use_ssl = False     # Set to True if using SSL/TLS

    # Create ISO format timestamps for the last 30 days
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=30)
    
    # Format timestamps as ISO strings
    start_time_iso = start_time.isoformat() + "Z"
    end_time_iso = end_time.isoformat() + "Z"

    try:
        # Create the client using a context manager
        with SalesforceClient(host=host, port=port, use_ssl=use_ssl) as client:
            # Example case IDs - replace with actual case IDs
            case_ids = ["case_id_1", "case_id_2"]
            
            # Get case details with pagination and time filtering
            response = client.get_salesforce_case_details(
                case_ids=case_ids,
                page_size=50,
                start_time=start_time_iso,
                end_time=end_time_iso,
                timeout=30.0  # 30 seconds timeout
            )

            # Process the response
            print("\nCase Details Summary:")
            print(f"History Records: {len(response.history)}")
            print(f"Feed Items: {len(response.feed_items)}")
            print(f"Emails: {len(response.emails)}")
            print(f"Contact Trace Records: {len(response.ac_contact_trace_records)}")

            # Example: Print some details from the feed items
            print("\nRecent Feed Items:")
            for item in response.feed_items[:5]:  # Show first 5 items
                print(f"\nType: {item.type}")
                print(f"Created: {item.created_date}")
                print(f"Title: {item.title}")
                if item.body:
                    print(f"Body: {item.body[:100]}...")  # Show first 100 chars

    except grpc.RpcError as e:
        print(f"RPC Error: {e.code()}: {e.details()}")
    except Exception as e:
        print(f"Error: {str(e)}")


if __name__ == "__main__":
    main()