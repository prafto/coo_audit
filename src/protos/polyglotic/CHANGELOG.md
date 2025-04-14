# Changelog for polyglotic

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 0.0.1

- Create first version of polyglot gRPC

### 1.0.0
- Fix TranslateQueryRequest to only take one input query

### 2.0.0
- Separate generic failure_reason field to more specific translation and validation failures in TranslateQueryResponse

### 2.1.0
- Added new rpc TranslateSnowflakeQueryHistory to process a day's worth of queries

### 3.0.0
- Move failure reason from request to response for TranslateSnowflakeQueryHistory

### 4.0.0
- Remove service client configs and use google date type

### 5.0.0
- Remove reserved fields and go back to common/date.proto

### 5.1.0
- Add user field to requests

### 5.2.0
- Add initial query event for polyglotic producer

### 5.3.0
- Add snowflake metadata fields to query event for polyglotic producer

### 5.4.0
- Add original user to submitted the query to query event

### 5.5.0
- Add snowflake warehouse for tracking in our query poller
