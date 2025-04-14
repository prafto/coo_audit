# Changelog for user_management_protobuf

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 0.2.10

- Add error charge photo evidence and consumer comments endpoint

### 0.2.9

- Add GetErrorChargePhotoEvidenceResolution API

### 0.2.8

- Add error charge proto object

### 0.2.7

- Add solved timestamp for support hub case

### 0.2.6

- Add error charge refund status and dispute difference

### 0.2.5

- Add Problem, Category, ConsumerExplanation

### 0.2.4

- Add OrderErrorCategories to mx_error_charge/common.proto

### 0.2.3

- Add user info to CaseDetails
- Add business name and ID to CaseOverview
- Add updatedDateRange to GetCasesRequest
- Include store and business id in GetCaseDetailsRequest for permission check

### 0.2.1

- Add a new field case_number to CaseOverview (case_number is different from case_id)

### 0.2.0

- Add GetMxSupportCasesV1 and GetMxSupportCaseDetailsV1 endpoints

### 0.1.6

- Add error_charge.proto file so that nested protos can be recognized

### 0.1.5

- Add tsproto to mx-support-service

### 0.1.4

- Deprecate GetDeliveryEligibilityForMerchantDispute
- Add common fields into ValidateAndCreateMxErrorChargePaymentAdjustment

### 0.1.3

- Create CxTransparencyService and GetCxSignals endpoint

### 0.1.2

- Added consolidated dispute submission endpoint for Mx Payment Adjustments

### 0.1.1

- Add mx_error_charge_dispute.proto and mx_error_charge_fraud_fact.proto

### 0.1.0

- Add HelloWorldService and SayHello endpoint
- Add CHANGELOG.md

### 0.0.1

- Initial commit to set up mx_support_service protobuf folder
