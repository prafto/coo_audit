# Changelog for aims_protobuf

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 0.1.5

- Upddate ModelVersionConfig proto:
- Include model bucket to the grpc

### 0.1.4

- Add Model Creation endpoint:
- Added CreateModelVersionConfig RPC to create individual model version configs
- Added GetModelById RPC to get a model version config by model id
- Added GetModelsByModelClassName RPC to get all model config versions of a model class

### 0.1.3

- Add Feature Creation Endpoint to new Service Endpoint

### 0.1.2

- Add Feature Creation Endpoint:
- Added CreateFeatureNode RPC to create individual feature nodes
- Added CreateFeatureSourceNode RPC to create feature source nodes with multiple features
- Added comprehensive request/response messages for feature node creation


### 0.1.1

- Add comprehensive feature metadata management system including:
- Feature schema definition with versioning support
- System tags for governance (PII, sensitive data, compliance)
- Detailed feature node structure with source tracking

### 0.1.0

- Add basic ai-metadata-service stub
- Add basic endpoints for Adding eventlog, feature, and source
- Add basic messages protobufs

### 0.0.1

- Add initial `helloworldServce` service
