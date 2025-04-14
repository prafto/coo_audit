# Changelog for user_management_protobuf

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

### 2.5.0

- Defining column metadata rules in proto

### 2.4.1

- Adding channel filtering support

### 2.4.0

- Adding APIs to insert data into CRDB for engineers only

### 2.3.0

- Adding DataPointStatus to DataPoint

### 2.2.0

- Adding CreateReportsV1 endpoint

### 2.1.0

- Adding hour of day and day of week product keys for Sales Insights M2

### 2.0.0

- Create a MonetaryFields64 type with unit amount in Int64
- Replace all MonetaryFields types by MonetaryFields64 in IRS

### 1.5.0

- Add id to Descriptors

### 1.4.0

- Add monthly sales insights product key to get sales data grouped by month

### 1.3.0

- Add last updated timestamp to GetKeyPerformanceIndicatorsV1Response

### 1.2.0

- Add data filters to GetKeyPerformanceIndicatorsV1Request

### 1.1.0
- Adding additional sales insights related product keys to distinguish for specific datasets. 
- This is to avoid returning overly large datasets (for example, 10 days = 240 hourly datasets if we do not have keys).

### 1.0.0

- Update GetDataSetsV1 endpoint with labels used for group bys
- Rename GetDataSetsV1 fields, deprecate some fields for new fields (through rename). Code not in production yet.

### 0.9.0

- Add GetDataSetsV1 endpoint 
- Add GetKeyPerformanceIndicatorsV1 endpoint 

### 0.8.0

- Add GetFiltersV1 endpoint with examples

### 0.7.0

- Adding enums and messages for IRS endpoints

### 0.6.0

- Add Descriptors to common.proto

### 0.5.0

- Add common.proto

### 0.4.0

- Add ProductKey proto file

### 0.3.0

- Add initial IRS core proto file

### 0.2.0

- Add CHANGELOG.md
- Add tsproto package support

### 0.1.0

- Add HelloWorldService and SayHello endpoint

### 0.0.1

- Initial commit to set up insight_reporting_service protobuf folder

