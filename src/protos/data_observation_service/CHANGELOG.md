# Description
## Protobuf to be consumed by data_observation_service
## Includes several services for data observation
## Watchtower Anomaly Detection https://doordash.atlassian.net/wiki/spaces/Eng/pages/3235054873/Watchtower

---

# Changelog for data_observation_service protobuf

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 0.0.2

- Add DataObservationService and ListWTMetricAnomalies rpc to service.proto

### 0.0.1

- Add initial data_observation_service folder and files -- release.json, CHANGELOG.md, service.proto
- Add `data_observation_service` to `protos.lst`
- Add initial response and request for `data_observation_service.proto`