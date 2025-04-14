### 0.0.39
Add pending validations review status. This is a new status that only SSS has, it doesn't exist in review service.

### 0.0.38
- Add OperationReviewComment

### 0.0.37
- Deprecate status parameter in CreateSchemaChangeOperationRequest and CreateGenericOperationRequest since it will now be handled by the server.

### 0.0.36
- Add comment field
- Add review to GetGenericOperationResponse

### 0.0.35
- Add new endpoints for storage control plane

### 0.0.34
- Add 2 new endpoints ApproveOperation, RequestChangeOperation for schema changes review
- Add OperationReview to GetSchemaChangeOperationResponse

### 0.0.33
- Added ValidationLevel enum to support warning level validations
- Added validation_level field to GetValidationResponse message
- Added validation_level filter to GetAllValidationsForOperationRequest for filtering validations by level

### 0.0.32
- Resources

### 0.0.23
- Add support for redis handler

### 0.0.22
- Rollback the buf validation because it causes build issues across our ecosystem

### 0.0.21
- Add `OperationType` to `CreateSchemaChangeOperationRequest`
- Add validation rule to only allow CRDB and Postgres operation types for above

### 0.0.20
- Split schema change `OperationType` into more specific CRDB and POSTGRES types
- Deprecate the old schema change operation type
- Add `pre_req_testing_environments` to `CreateSchemaChangeOperationRequest`

### 0.0.19
- Add awaiting-prereqs and failed statuses to validation status enum

### 0.0.18
- Return changefeed for resume/pause/delete changefeed operation

### 0.0.17
- Add changefeed create, pause, resume, cancel operations

### 0.0.16
- Change changefeed job id type to string

### 0.0.15
- Add updated_by fields

### 0.0.13
- add filter for ValidationType to `RunValidationsForOperation`

### 0.0.12
- Add GetAllOperations endpoint
- Add RunValidationsForOperation endpoint
- Add EventLog create and get endpoints

### 0.0.11
- Added "abandoned" to validation status enum list

### 0.0.10
- Added APIs for validations.

### 0.0.5
- Added CRUD APIs for schema change operations and validations.