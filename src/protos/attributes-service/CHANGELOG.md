# Changelog for attributes_protobuf
## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 0.0.1

- Add initial attributes_service folder and files -- release.json, CHANGELOG.md
- Add `attributes_service` to Makefile
- Add `attributes.proto` with initial iteration of AttributeService endpoint

### 1.0.1

- Replace AttributeFilter with map<string, ListOfFilterExpressions>
- Change dx_fields and dx_mx_fields to dx_field and dx_mx_field

### 1.0.2

- Add RankByAttribute

### 1.0.3

- Rename namespace -> Entity
- update enum with friendlyName
- Add dasher_id inside DasherAttributeKey

### 1.0.4

- Add java outer class
- update value for enum which matches DB columns

### 1.0.5

- Update field names for GetAttributesByFilterResponseField
- Update value for enum

### 1.0.6

- Update field type on UpdateDasherAttribute & UpdateDasherMerchantAttribute

### 1.0.7

- Update filter value type to FieldTypeAndValue

### 1.0.8

- Add address namespace

### 1.0.9

- Adding upsertCount to UpsertAttributeResponse 

### 1.0.10

- Adding vehicleType attribute to dasher entity

### 1.0.11

- Add AddressAttributeKey for address namespace

### 1.0.12

- Add EphemeralAttributeService API Definitions

### 1.0.13

- Add DataType field to EphemeralAttributeField 

### 1.0.14

- Fix int data type 

### 1.0.15

- Initial JobService API Spec

### 1.0.16

- Fix typos

### 1.0.17

- Adding AttributeType to BatchJob APIs

### 1.0.18

- Adding fraud composite score dasher attribute key

### 1.0.21

- Add attribute data type and key to JobMetadata

### 1.0.22

- Add attribute namespace to JobMetadata
- Adding SP Attributes to ephemeral api

### 1.0.23

- Change type from string to BatchJobRunState for job_run_state
- Change type from int64 to Timestamp for before and after

### 1.0.26

- Fix SP UpsertEphemeralAttributeRequest
- Fix version from int -> double
- Add version for stand upsert

### 2.0.0

- Introduce v2 APIs

### 2.0.1

- Add version to v1 Get APIs

### 2.0.2

- Remove version from v1 GET APIs

### 2.0.3

- Improve v2 UPSERT API format

### 2.0.4

- Add version to kafka events

### 2.0.5

- Add segmentation APIs

### 2.0.6

- Fix spDasherIdentifier typo

### 2.0.7

- Fix identifier filter bug

### 2.0.8

- Fix spDasherField naming

### 2.0.9

- Add timestamp to FieldValue

### 2.0.10

- Change spDasher to sdSpDasher

### 2.0.11

- Change spDasher to sdSpDasher part 2

### 2.0.12

- Add event for SdSpDasher segments

### 2.0.13

- Register UpsertSdSpDasherSegmentEvent

### 2.0.14

- Create batch job v2 to support segment API

### 2.0.15

- Use int64 instead of int32 for FieldValue integer

### 2.0.16

- Use int64 instead of int32 for segmentation API

### 2.0.17

- Introduce string list FieldValue type

### 2.0.18

- Introduce string list FieldType

### 2.0.19

- Remove string list FieldType and introduce Json Format String FieldType

### 2.0.20

- Introduce dimension 1 to ephmeral attributes

### 2.0.21

- Introduce dimension 1 to ephmeral attributes part 2

### 2.0.22

- Add DATA_SOURCE_TRINO

### 2.0.23

- Adding support for LxConsoleSegments

### 2.0.24

- Removing LxConsoleSegments from existing APIs
- Adding new API to support LxConsoleSegments

### 2.0.25

- Retire unused V1 API's

### 2.0.26

- Introduce Segment API v2

### 2.0.27

- Fix segment api v2 offset pagination

### 2.0.28

- Add support for dimensions1 on address and sp entity - ephemeral apis

### 2.0.29

- Add support for dimensions1 on address and sp entity - ephemeral kafka events

### 2.0.30

- Retire v1 segment API

### 2.0.31

- Adding support for batch job response sorting

### 2.0.32

- Changing Created/ModifiedDate to Start/EndTime on batchRunDetails api

### 2.0.33

- Adding support for JobServiceInternal.  API's used for cleaning up deleted jobs

### 2.0.34

- Adding support for Cart ephemeral entity.

### 2.0.35

- Adding uuid field to FieldValue structure

### 2.0.37

- Adding Support for Store Entity
- Adding PickScore as standard attribute

### 2.0.38

- Create proto for dx360

### 2.0.40

- Add segmentation API v3

### 2.0.41

- Adding job_id and run_date fields to batch_job_run_details api

### 2.0.42

- Adding support for Consumer ephemeral entity.

### 2.0.43

- Adding support for Submarket Weekly segments

### 2.0.44

- Adding SubmarketWaitlistSegmentEvent to register_schemas

### 2.0.45

- Adding SubmarketWaitlistSegmentEvent to register_schemas

### 2.0.46

- Adding DasherTaskHistorySegment and StoreItemSegment support to segment_v3 api

### 2.0.47

- Adding DasherTaskHistorySegment and StoreItemSegment support to segment_v3 api part 2

### 2.0.49

- Modify StoreItemSegment support to segment_v3 api
