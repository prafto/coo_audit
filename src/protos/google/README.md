These protobuf is consumed by UnifiedGateway Service.

Unified-gateway is a service acting as unified BFF which allows teams to expose GRPC as REST APIs. For those product teams who want to expose their RPC as REST API without coding in BFF, they can expose it through unified gateway by defining in service-protobuf repo.

Unified-Gateway will scan and load the whole service-protobuf repo for all services. We are using other tools rather than protoc, but it doesn't have the these protobuf. So we need to have a separate copy of these protobuf.
