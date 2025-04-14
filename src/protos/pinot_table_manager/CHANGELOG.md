# Changelog for pinot_table_manager

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 0.0.1

- Create first version of pinot_table_manager gRPC

### 0.1.0

- Add GetPinotInfo endpoint for information such as available Pinot tenants

### 0.2.0

- Add cluster to ResourceConfig to differentiate prod, v2, and qa
- Add ingestion filter to support ingestion filters
- Add encoding enum to support Avro vs Protobuf

### 0.2.1

- Add schema ID in InferSchemaResponse and in KafkaConfig
  - Pinot REALTIME tables with Protobuf-encoded Kafka topics require it. In PTM, we could fetch it
    from the Iguazu Schema Registry during config generation but that would make the generation
    stateful / non-static. This is a cleaner solution

### 0.3.0

- Add TableType enum's for OFFLINE APPEND, OFFLINE REFRESH, and hybrid tables
  - Could make this just REALTIME / OFFLINE and have support elsewhere, but IMO that would make
    PTM's abstractions too close to Pinot

### 0.3.1

- Deprecate `is_str_format` since rollups are now generated as `TIMESTAMP` data types
- Add Code for invalid tables

### 0.4.0

- Add gRPC endpoint to fetch messages from topic

### 0.5.0

- Deprecate GetKafkaInfoResponse `topics` and change to Protobuf map

### 0.6.0

- Create ConvertTableRequest for generating table configs (previously used CreateTable)
- Add Infra Service change request ID to CreateTableResponse

### 0.7.0

- Add partition, offset, and decoder_class fields to GetKafkaMessagesRequest

### 0.7.1

- Make offset int64 so that -1 can be specified. This type change is allowed.
