# Nexus Protos

This repository contains the protocol buffers (protos) used for the Nexus service. It defines the messages and services for communication between different components of the system.

## Best Practices

### Use `protovalidate` for Validation

Whenever applicable, use the `protovalidate` library to ensure the validity of incoming and outgoing data. This provides automatic validation for your proto messages and reduces boilerplate validation code. Integrating validation within the protobuf schema helps keep the service logic clean and consistent.

Example:

```protobuf
message Request {
    string param1 = 1 [(validate.rules).string.min_len = 1];
    repeated string params2 = 2 [(validate.rules).repeated.min_items = 1];
}