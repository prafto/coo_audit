# Changelog for pinot_service

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 0.0.1

- Create first version of pinot_service gRPC

### 1.0.0

- Add missing name column for request, remove table_configs_json
- Change units for some column e.g. float for estimated_qps
