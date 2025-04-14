# Changelog for wait list protobuf

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 0.0.8

- Add a new entity type - Market in the waitlist service for quest diagnostics pilot launch

### 0.0.1

- Add initial waitlist_protobuf folder and files -- release.json, CHANGELOG.md
- Add `waitlist_service` to Makefile
- Add `waitlist_service.proto` with a random endpoint
