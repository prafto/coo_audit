## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 1.0.0

- Setup new service
- Add new rpcs

### 1.2.1

- Add arguments field in executeAutomation

### 1.3.0
- Update ERS dependency

### 1.4.0
- Update ERS dependency that removes copy_values field in SupportWorkflowNode

### 1.4.1
- Add metadata field in the request

### 2.0.0
- Add Test Framework endpoints
- Point to latest ers proto version

### 2.1.0
- Add update apis on test framework

### 2.1.1
- Add created_at, updated_at, created_by, updated_by fields to test_config and workflow_test_config

### 2.2.0
- Replace metadata with result_metadata in ExecuteWorkflowTestResponse

### 3.0.0
- Add contracts for Workflow Test Suite executions and update existing contracts to include workflow version

### 4.0.0
- Change get apis to strictly include workflow_id and workflow_version

### 4.1.0
- Update experience_reliability_service version

### 5.0.0
- Rename getTestParameters to getTestBaseConfigs

### 6.0.0
- Major refactor to reflect UI design and terminologies

### 6.0.1
- Added comments on suite metadata

### 6.1.0
- Add GetWorkflowTestSuite api

### 6.2.0
- Move description inside metadata

### 6.3.0
- Added Map of custom_input_field_values to ExecuteAutomationRequest to pass manualStep custom Fields

### 6.3.1
- simply bumping version since the task for creating 6.3.0  version got skipped

### 6.3.2
- added "workflow_platform.proto" to the workflow_platform package
- added "getNodeExecutionEvents" rpc & relevant messages
- TODO: deprecate "GetAutomationLogEntries" from the workflow_platform.proto file in the ers package 

### 6.4.0
- Remove test_config_uuid on update workflow test suite request

### 6.5.0
- Put back description as main field of workflow_test_suite

### 7.0.0
- Simplify Test Scenario Result

### 7.1.0
- Rename workflow_test_result_uuid to test_scenario_result_uuid

### 7.2.0
- Add CopyTestSuites rpc

### 7.3.0
- fix type target_workflow_version

### 7.4.0
- Add Delete TestScenario

### 7.5.0
- Add GetWorkflowUserTypes

### 7.6.0
- Add GetWorkflowBaseConfigs

### 7.7.0 
- Add latest_test_execution_result in test_scenario

### 7.8.0
- Increase threshold on executeAutomation

### 7.9.0
- Change TestScenarioResult with TestScenarioSummary

### 7.10.0
- Add is_success field on delete rpcs

### 7.11.0
- Rename test_scenario_uuid to test_scenario_result_uuid

### 7.11.2
- Added workflow_step_execution_metadata_list to ExecuteAutomationResponse 

### 7.12.0
- Add new field in ExecuteAutomationRequest

### 7.12.1
- Bumping version of experience_reliability_serviceASA

### 7.13.0
- Add new api GetNodeWorkflowStepExecutionMetadata in workflow-platform
- Updated NodeExecutionEvent with new data fields workflow_version,user_id,email_id and workflow_step_metadata_uuid

### 7.13.1
- Add new fields to testScenarioSummary

### 7.14.0
- Update GetWorkflowTypes API

### 7.14.1
- Update ERS version

### 7.15.0
-  Added new apis for workflow jump and automation dependency

### 7.15.1
-  Added update api for workflow jump and automation dependency for backward compatibility

### 7.16.0
- Added new rpc to support workflow config migration

### 7.17.0
- Updated workflow config migration contract

### 7.20.0
- Added GetWorkflowTHQRolloutConfiguration and CreateOrUpdateWorkflowTHQRolloutConfiguration contract

### 7.20.1
- Added DeleteWorkflowThqRolloutConfiguration rpc contract

### 7.21.0
- Add GetWorkflowUuidByWorkflowId endpoint

### 7.21.1
- Add GetWorkflowTypesByWorkflowIds endpoint

### 7.21.2
- Add workflow_type filed to NodeExecutionEvent

### 7.21.3
- Add workflow_name to filed to ThqWorkflowRolloutConfiguration

### 7.22.0
- Add new enum MtrResolutionTag

### 7.23.0
- Add new rpcs to support test coverage feature

### 7.23.1
- Adding GetWorkflowsByWorkflowTypes api

### 7.23.2
- Adding UG annotations to ExecuteTestSuiteCollection

### 7.24.0
- Add new fields to GetWorkflowBaseConfigs API
- Remove duplicate rpc

### 7.25.0
- Add DeleteChangelog API

### 7.28.0
- Add tenant field to NodeExecutionEvent

### 7.30.0
- Replace tenant field of type Tenant in NodeExecutionEvent with tenant_id field of type String

### 7.38.0
Add API ExecuteContextBasedWorkflowAsync

### 7.38.1
Increase Playground timeout to 5min

### 7.38.2
Forward Sub-client-service-name header from UG at the service level

### 7.39.0
Add ExecuteManualDecisionAutomation to WorkflowPlatformExtendedService
