# Changelog for release_coordination (RCS) protobuf

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---
### 1.27.0
- Add `SPINNAKER_PIPELINE_ACTION_GRAPH_DEPLOY`, `SPINNAKER_PIPELINE_ACTION_GRAPH_EMERGENCY_DEPLOY` and `SPINNAKER_PIPELINE_ACTION_GRAPH_BOUNCE` actions to `SpinnakerPipelineAction` enum
- Update `ReleaseCoordinationService` to include Graph Config endpoints

### 1.26.0
- Create `GetConfigTagByPullRequestId`

### 1.25.0
- Add `SPINNAKER_PIPELINE_ACTION_DEPLOY` action to `SpinnakerPipelineAction` enum

### 1.24.0
- Create `GetAllGlobalDeployFreezeConfigs`
- Create `GetServiceDeployFreezeConfig`
- Create `UpsertGlobalDeployFreezeConfig`
- Create `UpsertServiceDeployFreezeConfig`
- Create `UploadGlobalDeployFreezeConfigToS3`

### 1.23.0
- Create `GetAllServiceConfigs` and `GetAutoDeployServiceNames`

### 1.22.0
- Create `GetDeployMetadata` and `DeployMetadata`

### 1.21.0
- Add `UpsertRollbackData`
- Add `rollback_id`, `is_latest`, `config_version` and `previous_config_version` to `DeployData`
- Add `pipeline_id` and `pipeline_id_to_rollback` to `GetRollbackDataRequest`

### 1.20.0
- Add `environments` and `sandbox_environments` to `ServiceConfig`

### 1.19.0
- Add `use_automatic_deployment` to `ServiceConfig`

### 1.18.0
- Add `UpdateServiceConfigBundles` to update bundles in service_configs

### 1.17.0
- Add `pipeline_types` to `GetDeployDataListRequest`

### 1.16.0
- Add `triggered_by` to `DeployData`

### 1.15.0
- Create `RollbackConfig`, `GetRollbackConfig`, `GetAllServiceRollbackConfigs`, `UpsertRollbackConfig`
- Create `RollbackData`, `GetRollbackData`, `GetRollbackDataList`

### 1.14.0
- Add `SPINNAKER_PIPELINE_ACTION_SANDBOX_DEPLOY` to `SpinnakerPipelineAction`
- 
### 1.13.0
- Add `SPINNAKER_PIPELINE_ACTION_BACKFILL_LKG` action to `SpinnakerPipelineAction` enum

### 1.12.0
- Add pipeline_type to `DeployData`

### 1.11.0
- Create `SendSpinnakerEventByCaller` to allow triggering Spinnaker pipeline by a caller

### 1.10.1
- Add repo_name to `DeployData`

### 1.10.0
- Update `DeploySchedule` by adding fields: `is_automatic_deploys_active`, `is_cron_deploys_active`

### 1.9.1
- Add previous_tag to `DeployData` and errors to `SpinnakerPipelineData`

### 1.9.0
- Create `GetSpinnakerPipelineDataListRequest`

### 1.8.0
- Add parent_pipeline_id to `GetSpinnakerPipelineDataRequest`

### 1.7.0
- Add parent_pipeline_id and pipeline_name to `SpinnakerPipelineData`

### 1.6.1
- Update api docs. No functional changes.

### 1.6.0
- Add go client

### 1.5.0
- Create `UpdateBuildDataLockStatus`

### 1.4.0
- Update `ServiceConfig` by adding fields: `is_cron_deploys_active`, `cron_deploys_comment`

### 1.3.2
- Add pipeline_name in `DeployData`

### 1.3.1
- Add bundle deployment flag in `GetDeployDataListRequest`

### 1.3.0
- Create `BuildData`, `GetBuildData`, `UpdateBuildData`, `GetBuildDataList`
- Create `DeployData`, `GetDeployData`, `GetDeployDataList`
- Create `SpinnakerPipelineData`, `GetSpinnakerPipelineData`

### 1.2.0
- Create `SpinnakerEvent`, `GetSpinnakerPipelineActionParams`, `SendSpinnakerEvent`

### 1.1.0
- Create `ServiceConfig`, `GetServiceConfig`, `GetAllServiceConfigs`, `UpdateServiceConfig`
- Create `DeploySchedule`, `GetDeploySchedule`, `GetAllServiceDeploySchedules`, `UpsertDeploySchedule`
- Create the following to support `DeploySchedule`: `ScheduleWindow`, `ScheduleTime`, `DayOfWeek`

### 1.0.0
- Remove placeholders `GreeterService`, `SayHelloRequest` & `SayHelloResponse`
- Create `ReleaseCoordinationService`
- Create `GlobalConfig`, `GetGlobalConfig`, `GetAllGlobalConfigs`, `UpsertGlobalConfig`, `GetGlobalConfigList`

### 0.0.1
- Add initial release_coordination folder and files -- release.json, CHANGELOG.md
- Add `GreeterService`, `SayHelloRequest` & `SayHelloResponse` as placeholders.
