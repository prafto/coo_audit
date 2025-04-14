# Changelog for Reliability Scorecard protobuf.

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 1.2.0
- Added RPC for retrieving scorecards by owner team.

### 1.1.0

- Added RPC for retrieving project scorecards in bulk.
- Added RPC that returns a list of checks that projects are evaluated against.

### 1.0.0

- Added RPC for retrieving the historical information for a project's scorecard.

### 0.0.2

- Added `reason` to indicate why a check failed or was partially successful.

### 0.0.1

- Added initial definitions for RPCs and message types.
