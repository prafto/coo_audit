# Changelog for incident_service__protobuf

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 0.0.1

- Add initial incident_service folder and files -- release.json, CHANGELOG.md
- Add `incident_service` to Makefile
- Add `incident.proto`

### 0.0.2

- Changed incident object
- Changed out Incident Type for Enum

### 0.0.3

- Changed severities, swapped `level` and `scope` to align better with the db and incident service

### 0.0.4

- Changed the zoom_meeting_data from `bytes` to `string`. Will be base64 encoding the json instead of converting to a byte array

### 0.0.5

- Added enum for incident state, i.e. Active / Mitigated / Resolved
- Added timestamp for the next notification time

### 0.0.6

- Added filter message

### 0.0.7

- Correctly implemented filter

### 0.0.8

- Broke out the reporter into a message, added enum to capture reporter location, i.e. slack, devconsole ...
- Changed the severity level from a string to an enum

### 0.0.9

- Added Javascript support

### 0.0.10

- Added Typescript support

### 0.0.11

- Added filter option for the declared datetime

### 0.0.12

- Updated some naming

### 0.0.13

- Update team info

### 0.0.14

- Added CreateIncident support
