# Changelog for traffic control plane

## In `release.json`, increment the tag like so

### Given a version number MAJOR.MINOR.PATCH, increment the

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---
### 0.0.34

- Remove AZ draining start and end function

### 0.0.33

- Make AZ draining weight error handling more detailed

### 0.0.32

- Add Sampling into Cache Advisor 

### 0.0.28

- Update AZ draining weight change APIs to include failed to update services in response and some other fields

### 0.0.28

- Add Cache Advisor Into Egress

### 0.0.27

- Update TestTrafficRouting - add on_egress support

### 0.0.26

- Add safe regex to StringMatcher

### 0.0.25

- Add AZ draining weight change related APIs

### 0.0.24

- Add Midr Routing

### 0.0.23

- Add notification preferences type and add to Onboard API

### 0.0.22

- Add placement to change requests

### 0.0.21

- Add placements to onboard

### 0.0.20

- Add is_fully_in_cell field for migration status response

### 0.0.19

- Add create mesh override

### 0.0.18

- Add Outlier Detection field to Ingress and IngressDefaults

### 0.0.17

- Change supercell migration status proto to be per-cell

### 0.0.16

- Add Outlier Detection types

### 0.0.15

- Move common types to common.proto
- Change strings to StringValues

### 0.0.14

- Add Supercell Migration APIs

### 0.0.13

- Change slow start enabled type to BoolValue

### 0.0.12

- Add OnboardMeshService RPC

### 0.0.11

- Bump version

### 0.0.10

- Add Requester

### 0.0.9

- Add MeshConfigIdentifier

### 0.0.8

- Add GetMeshServiceConfig rpc

### 0.0.7

- Add GetMeshServices rpc

### 0.0.6

- Add weight to Endpoint

### 0.0.5

- Add AZ information to Endpoint

### 0.0.4

- Add tsproto package support

### 0.0.3

- Fix num endpoints

### 0.0.2

- Add TCP service, common enums, and GetDDSDServices

### 0.0.1

- Add initial traffic control plane service with -- release.json, CHANGELOG.md
