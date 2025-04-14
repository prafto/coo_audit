# Changelog for configuration-service

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---
### 0.5.29
Add new configs merchant level media configs

## 0.5.28
Add new configs to mp provider metadata

### 0.5.27
Add new configs for Partner Settings projects

### 0.5.26
Add SSIO Activation config field

### 0.5.25
Add Onboarding Activate Store config to manage configuring ssio activation

### 0.5.24
Add Integration Platform Type config to MpProviderMetadataGeneral

### 0.5.23
Add LiveOrderManagementPluginFeatureConfig to manage configuring pos plugin features

### 0.5.22
Add is_recipient_name_enabled_after_dx_arrival_at_cx toggle in drive webhook

### 0.5.18
Add OFF type for PinDeliveryRuleType in fulfillment constraints

### 0.5.18
Add is_photo_on_delivery_enabled toggle to fulfillment constraints

### 0.5.17
Adding pincode and order volume transform in drive fulfillment constraints

### 0.5.16
Adding cbd config in drive fulfillment constraints

### 0.5.15
Adding new otc med parameters in drive form

### 0.5.14
Adding a new configuration for drive form

### 0.5.13
Adding new adhoc scripts create method

### 0.5.8
Add a drive priority pay config in configType proto

### 0.5.6
Add a drive order rejection config in configType proto

### 0.5.5
Add a drive bad address constraint

### 0.5.3
Add a new expected onboarding flow type - EPM

### 0.5.0
Add new property for fulfillment constraint for enabling reject bad adderss orders

### 0.4.9
Add new type for middleware_subtype

### 0.4.8
Deprecating duplicate provider privacy url

### 0.4.7
Add new requested px metadata field

### 0.4.6
Fixing px metadata from breaking py types

### 0.4.5
Update provider metadata model - fix enum value typo

### 0.4.4
Update provider metadata model - onboarding flow field

### 0.4.3
Update provider metadata model based on latest request

### 0.4.2
Add integration metadata model

### 0.4.1
Adding new default item prop fields, deprecating old ones

### 0.4.0
Fixing integrations enums

### 0.3.8
Add new config type mx integrations order

### 0.3.7
Seattle compliance

### 0.3.6
Add new SMS types to cx_comms

### 0.3.5
Add extra fields for permission for createConfig

### 0.3.4
- Add mx integrations configs + px entity type

### 0.3.3
- Add is_allowed

### 0.3.2
- MX Tablet config

### 0.3.1
- Cadence retry policy config

### 0.3.0

- Parcel config

### 0.2.9

- Fixing mx user setting name

### 0.2.7

- Adding User entity type and user settings configuration

### 0.2.6

- Update the payload of dsx config

### 0.2.5

- Add snack to sof pay boost config day parts

### 0.2.4

- Add sof pay boost config

### 0.2.3

- Add CnG config

### 0.2.2

- Add customer_loyalty_number to developer's DSX config

### 0.2.1

- Add config for developer's DSX settings, used by delivery simulator

### 0.2.0

- Deprecating return config

### 0.1.0

- Deprecating alcohol configs, adding new ones

### 0.0.9

- Use bool optional for webhook configs

### 0.0.8

- Add drive dasher configs

### 0.0.7

- Add additional fulfillment constraint configs

### 0.0.6

- Add drive webhook

### 0.0.5

- Add alcohol

### 0.0.4

- Required optional

### 0.0.3

- Add version to Cx Comms

### 0.0.2

- Add entities

### 0.0.1

- Add initial configuration_service folder and files -- release.json, CHANGELOG.md
- Add `merchant_configuration_service` to Makefile
- Add `configuration_api.proto` with initial endpoints
