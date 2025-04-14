# Changelog for user_management_protobuf

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---
### 7.3.28

- Add PERMISSION_DEV_PORTAL_INVENTORY_VIEW and PERMISSION_DEV_PORTAL_INVENTORY_EDIT to Permission

### 7.3.27

- Add new string list field to shadow_log

### 7.3.26

- Add permission PERMISSION_MX_PORTAL_SUPPORT_HUB_VIEW

### 7.3.25

- Add userInfo to shadow proto.

### 7.3.24

- Add Permission PERMISSION_DEV_PORTAL_FEATURE_VIEW.

### 7.3.23

- Add PERMISSION_DEV_PORTAL_CATALOG_VIEW and PERMISSION_DEV_PORTAL_CATALOG_EDIT to Permission

### 7.3.22

- Add inject_user_roles to ListUserProfileMemberships.

### 7.3.21

- Add shadow log proto for CheckModelsAccess

### 7.3.20

- Add ROLE_DEV_PORTAL_SUPPORT user role for Dev Portal

### 7.3.19

- Allow MX_USER to access ListUserProfileMemberships

### 7.3.18

- Create PERMISSION_ANY catch-all permission

### 7.3.17

- Create PERMISSION_MX_PORTAL_MENU_HOURS_VIEW and PERMISSION_MX_PORTAL_MENU_HOURS_EDIT permission to allow view/edit access to Menu Hours in Mx Portal

### 7.3.16

- Remove redundant field `is_self_request` from GetUserProfile endpoints

### 7.3.15

- Add new field to existing UMS endpoints for authentication

### 7.3.14

- Update/add fields to receive adding/removing store_ids for CreateOrUpdateUserProfile endpoint

### 7.3.13

- Creating PERMISSION_ADS_MANAGER_ENTITY_ONBOARDED - a permission to denote whether an entity is onboarded to ads manager

### 7.3.12
- Move boolean option out of identifier

### 7.3.11
- Add option to include Entity information in UserProfileMembership response

### 7.3.10
- Add Model field to CreateOrUpdateUserProfileRequest

### 7.3.9
- Adding a flag to exclude model users when listing profiles of associated entities

### 7.3.8

- Update UserProfile with UpdatedAt timestamp

### 7.3.7

- Update CreateOrUpdateUserProfileRequest with store_ids field

### 7.3.4

- Introducing SetEntityLevelPermission - a new API to set a permission at the entity level

### 7.3.3

- Adding ENTITY_FIELD_ENTITY_LEVEL_PERMISSIONS to EntityField enum

### 7.3.2

- Add one single missed ads manager permission and deprecate one single missed ads manager permission

### 7.3.1

- Undo deprecation of permissions using "reserved" and instead use [deprecated = true]

### 7.3.0

- Add all new ads manager permissions (as part of full-serve migration from Campaign Manager)

### 7.2.0

- Change entity to model in checkCanEditUserProfileRequest

### 7.1.0

- Add list user profiles of associated entities cursor, limit, query, filter, sort by

### 7.0.0

- Rename requested_permission_info and role in CheckCanEditUserProfile
- Add field entity to CheckCanEditUserProfile
- Remove source

### 6.5.0

- Add list user profiles of associated entities rpc

### 6.4.0

- Add is_test to ES entity
- Add business_vertical_id to ES business attributes
- Expose ancestors in ES entity

### 6.3.0

- Added RPC endpoint CheckCanEditUserProfile

### 6.2.0

- Deprecated user_profile and added user_profile_with_entity in CreateOrUpdateUserProfileResponse

### 6.1.1

- Added PERMISSION_ADS_MANAGER_PAYMENT_METHOD_ENABLE_INVOICING to permissions

### 6.1.0

- Added RPC endpoint GetUserProfilesWithModelAccess

### 6.0.3

- Added ROLE_ADS_MANAGER_ANALYST to Roles

### 6.0.2

- Added business_employee_store_membership_id to UserProfileMembership

### 6.0.1

- Added ListUserProfilesWithOffset endpoint

### 6.0.0

- Added is_member_of_all_entities to contracts.
- [BREAKING CHANGE] Remove user profile options for CreateOrUpdateUserProfile. Only return UserProfile.

### 5.20.1

- Added Ads Manager view payment method page permission

### 5.20.0

- Added new CreateOrUpdateUserProfile endpoint

### 5.19.2

- Added Mx Portal create/edit marketing campaigns permisison

### 5.19.1

- Add Ads Manager payment method page permission

### 5.19.0

- Add ability to exclude drive only stores in search service

### 5.18.0

- Added 1 new permission for change of ownership

### 5.17.0

- Added support for Sort and Filter to List User Profile

### 5.16.0

- Added provider config permissions

### 5.15.0

- Added layout to IdentityUserCreationMetadata

### 5.14.1

- Adding Ads Manager admin and marketer roles

### 5.14.0

- Added MDS Business Employee Profile fields to User Profile message

### 5.13.0

- Added country shortname to kafka message

### 5.12.0

- Added iterable_data_fields to IdentityUserCreationMetadata

### 5.11.0

- Added country_shortname to address

### 5.10.0

- Added rpc endpoint to handle retry sending emails to existing users

### 5.9.1

- Added 3 new Permissions related to User Management for Ads Manager

### 5.9.0

- Updated IdentityCreationMetadata with a configuration_id

### 5.7.0

- Added ListUserProfilesWithMembership endpoint

### 5.6.0

- Changed ListUserProfileMemberships to accept Model as a parameter

### 5.5.0

- Updated CreateUserProfileRequest with identity user creation metadata for welcome emails
- Updated CreateUserProfileResponse with flag to let user know if an identity user already existed

### 5.4.0

- Added endpoint to fetch User Profile Membership by Business Employee Store Membership Id (MDS Legacy)

### 5.3.0

- Added endpoint to fetch User Profile by Business Employee Profile Id

### 5.2.2

- Add model name to SyncModelEvent.

### 5.2.1

- Add permissions for start page in developer.

### 5.1.1

- Add userId to CreateUserProfile API.

### 5.2.0

- Add model sync event proto

### 5.1.0

- Add GetMerchantUserInfoByUserId API

### 5.0.0

- Updated GetUserProfile to accept User Id and Model as a parameter to fetch by

### 4.0.2

- Add more roles.

### 4.0.1

- Add user profile roles in the ListUserProfiles response.

### 4.0.0

- Add Mx Portal and MDS permissions.

### 3.1.3

- Add roles and permissions for Dev Portal.

### 3.1.2

- Add MANIFEST.in file

### 3.1.1

- Add cursor to ListUserProfilesResponse

### 3.1.0

- Entity service

### 3.0.1

- Add model, unified parents, and unified ancestors to EntityField
- Add parents to entity

### 3.0.0

- Add user_profile_id into UpdateUserProfileRequest
- Update offset to cursor for ListUserProfilesRequest
- Add string query to filter results in ListUserProfilesRequest

### 2.0.1

- Add starting_point_id, submarket_id, and market_id to store attributes.

### 2.0.0

- Return UserProfileWithEntity for GetUserProfile

### 1.0.4

- Updated Permission enum to have shared, Mx Portal specific, and Ads Manager specific permissions.

### 1.0.3

- Update entity field enum and documentation.
- Change StoreAttributes is_franchised to franchise_organization_id
- Update total_results to be a long instead of an int

### 1.0.2

- Added UpdateUserProfile endpoint
- Added GetUserProfile endpoint

### 1.0.1

- Added identity data to CreateUserProfileRequest
- Added entity data to ListUserProfileResponse

### 1.0.0

- Created new common folder
- Moved user profile objects into common/user_profile.proto
- Moved permission enum to its own common/permission.proto
- Moved multi search filter objects into common/search.proto
- Moved entity objects into common/entity.proto
- Made enum field for search a string to be more generic

### 0.1.0

- Introduce SearchService with SearchEntities API

### 0.0.3

- Add CRUD user_profile endpoints
- Add CRUD user_profile_membership endpoints
- Add CRUD user_profile_role endpoints
- Add access check endpoints for permissions and models
- Removed unused `user_management.proto`
- Add `common.proto` to hold common UMS proto objects

### 0.0.2

- Add AddUserProfileRole endpoint to permission subservice

### 0.0.1

- Add initial bootcamp_service folder and files -- release.json, CHANGELOG.md
- Add `user_management_service` to Makefile
- Add `user_management.proto` with initial iteration of SayHello endpoint
