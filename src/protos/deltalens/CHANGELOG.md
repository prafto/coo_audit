# Changelog for deltalens

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 0.0.1

- Add initial deltalens folder and files -- release.json, CHANGELOG.md
- Add `deltalens` to Makefile
- Add `service.proto` with initial iteration of GetTableSnapshotResponse endpoint

### 0.1.0

- Update GetTableSnapshotResponse to include table statistics and table files
- Update GetTableSnapshotRequest to include only the fully qualified table path.

### 0.2.0

- Update GetTableSnapshotRequest to support table referrence (database + table name) as identifier

### 0.3.0

- Add GetTablePartitions to support table partitions availability.

### 0.4.0

- Add GetTableUserMetadataRequest to support table metadata and lineage metadata.

#### 0.4.1

- [Bug Fix] Add missing GetTableUserMetadata API

### 0.5.0

- Add MigrateDeltaTableToIcebergTable endpoint to migrate delta tables to iceberg tables
- Add MigrateDeltaTableToIcebergTableRequest for migration inputs
- Add MigrateDeltaTableToIcebergTableResponse for migratin output

### 0.7.0 

- Add GetTableSnapshotMetadata endpoint that uses delta kernel 
- Add GetTableSnapshotMetadataRequest for v2 endpoint that uses delta kernel 
- Add GetTableSnapshotMetadataResponse for v2 endpoint that uses delta kernel 

### 0.8.0 

- Add a version field to the GetTableSnapshotRequest

### 0.9.0 

- Add table format field to the GetTableSnapshotResponse

### 0.10.0

- Add catalog name field to table name 

### 0.11.0

- Add rpc for getting last updated at for a table's data and table information 