# Changelog for drive_order_service

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---

### 0.29.2
- Add BatchAddTaskServiceIdsForDriveOrder endpoint

### 0.29.1
- Add return_task_group_id for GetTaskServiceIdsForDriveOrderResponse

### 0.29.0
- Add return_task_group_id in AddTaskServiceIdsForDriveOrderRequest for return back tracking
- Add GetWorkflowInfoByTaskGroupIds API to support return flow


### 0.28.0
- Add SubstituteItemMetadata substitute_items_metadata to SubstitutionPreference

### 0.27.0
- Add created_at field to DriveOrderEntry

### 0.26.0
- remove Drive Order Service CBs

### 0.25.0
- Split the items update api's and update the circuitbreaker config across dos.

### 0.24.0 
- Change circuit breaker settings.

### 0.23.0
- Update items update API to flag if barcode should also get updated.

### 0.22.1
- Adding drive_order entry field for create

### 0.22.0
- Create GetOrCreateDeliveryDriveInfoEntry API and also remove deprecated fields from DriveQuote.

### 0.21.1
- remove unused fields from CreateDriveOrderEntryRequest

### 0.20.0
- Add UpdateDeliveryItemEntries API

### 0.19.0
- change type of allowed_vehicle_types from string to list of strings
### 0.17.0
- Modify `CreateDeliveryDriveInfoEntry` API

### 0.16.1
- Add barcode to request for delivery_item

### 0.15.0
- Update drive quote service calls to match drive service.

### 0.14.0
- Add field mask for customer_pii update 

### 0.13.0
- Add field mask for update

### 0.12.0
- Update create quoted estimates entry to simply pass the entry instead of each individual field.

### 0.11.1
- add field to update request

### 0.11.0
- Add final fields to quoted estimate entry

### 0.10.0
- Add additional fields to createCheckoutAudit

### 0.9.0
- Add missing fields for QuotedEstimateEntry data

### 0.8.1
- Version bump to retry build

### 0.8.0
- Add merchant_recommended_substitute_external_ids to SubstitutionPreferences

### 0.7.1
- Add delivery_creation_extra_params to CreateDriveDeliveryRequest, UpdateDriveDeliveryRequest

### 0.7.0
- Add missing fields to UpdateDriveDeliveryRequest

### 0.6.0

- Bump up proto version

### 0.5.4

- Add fields to CreateDriveOrderEntryRequest

### 0.5.3

- Update parameter audit_successful naming in CreateDriveCheckoutAuditStatusByExternalDeliveryIdRequest

### 0.5.0

- Add DriveCheckoutAuditService proto and rpc's

### 0.4.18

- Add order status to event history on parcel service

### 0.4.17

- Add getOutageRefundDriveOrders API for DOS migration

### 0.4.16

- Add tobacco, hemp, otc fields to DriveCreationExtraParams

### 0.4.12

- Add event_history to DriveParcelMidmileInfoEntry

### 0.4.11

- Add pin_code metadata to DeliveryCreationExtraParams

### 0.4.6

- Add rpc GetParcelOrderByBarcode to DriveParcelService

### 0.4.5

- Update commission rate to nullable, allowed vehicle to list of strings

### 0.4.4

- Add missing fields in DriveOrder -- Parcel and DSX related fields

### 0.4.3

- Add missing fields in DriveOrder -- OrderItem

### 0.4.2

- Add missing fields in DeliveryExtraParams

### 0.4.1

- Add ID to delivery_state_change entry

### 0.4.0

- Add item substitution preference rpc

### 0.3.14

- Add driver_zero_tip_details in CreateDriveOrderEntryRequest

### 0.3.8

- Fix comment for delivery_tracking_urlcode

### 0.3.7

- Add Requests/Responses for DriveOrderService

### 0.3.6

- Rename origin address id to origin facility id due to product request

### 0.3.5

- Add dimensions to the delivery_item table and add API to fetch midmile provider's tracking ID

### 0.3.4

- Add isGeneric to Address proto

### 0.3.3

- Add Requests/Response for DeliveryItemService

### 0.3.2

- Update parcel.proto to update the parcel status details to stringValue since it is an optional field in the update API

### 0.3.1

- Update parcel.proto to update the parcel status details to stringValue since it is an optional field

### 0.3.0

- Add kotlin artifacts

### 0.2.31

- Add proto for drive parcel midmile info entry

### 0.2.30

- Add common proto for drive_order_service

### 0.2.29

- Add CreateQuotedEstimateEntry in QuotedEstimateService

### 0.2.28

- Fix id type for delivery_customer_pii.proto

### 0.2.27

- Add delivery_customer_pii.proto

### 0.2.26

- Add DeliveryCreationExtraParams and updated_at timestamp

### 0.2.25

- Bump version to build kotlin artifacts

### 0.2.24

- Add DriveQuoteAcceptanceService

### 0.2.23

- Add DriveQuoteService.CreateDriveQuoteEntry

### 0.2.22

- Add special_instructions in DeliveryItemEntry

### 0.2.21

- Add more fields to DriveDeliveryService.UpdateDelivery

### 0.2.20

- Add rpc UpdateDriveDeliveryStateChangeEntryPayload to DriveDeliveryStateChangeService

### 0.2.19

- Add rpc GetMostRecentDeliveryItemByBarcode to DeliveryItemService, and remove rpc CheckIfBarcodeExist

### 0.2.18

- Add rpc CheckIfBarcodeExist to DeliveryItemService

### 0.2.17

- Add rpc GetDeliveryItemEntriesByBarcode to DeliveryItemService

### 0.2.16

- No changes; empty commit to re-attempt publishing of the artifacts

### 0.2.15

- Add DriveDeliveryService/UpdateDeliveryAsync RPC

### 0.2.14

- Add Item and Customer to Drive Order Entry

### 0.2.13

- Add dasher_confirmed_time, abandoned_at, cancelled_at, shift_id to Delivery message

### 0.2.12

- Update GetDriveOrderEntryByRedeliveryId API to use int64 and return a list

### 0.2.11

- Add RedeliveryId field and GetDriveOrderEntryByRedeliveryId API

### 0.2.10

- Add GetDriveOrderByUrlCode API

### 0.2.9

- Add Dasher (and nested Vehicle) to GetDriveOrder's Delivery

### 0.2.8

- Add Dasher (and nested Vehicle) to UpdateDriveDeliveryRequest

### 0.2.7

- Add more fields to UpdateDriveDeliveryRequest

### 0.2.6

- Update DriveOrderEntry: fix incorrect fields

### 0.2.5

- Update DriveOrderEntry: add all fields

### 0.2.4

- Update DriveQuoteService: make quote_id a string

### 0.2.3

- Add DriveQuoteService and QuotedEstimateService APIs

### 0.2.2

- Add DriveOrderEntry to GetDriveOrder

### 0.2.1

- Update EtaDataService: make fields non-null

### 0.2.0

- Add GetDriveOrderService APIs

### 0.1.0

- Add DriveDeliveryService.UpdateDelivery including only required fields in request

### 0.0.9

- Add eta_data.proto

### 0.0.8

- Add bundle_key in DeliveryItemEntry

### 0.0.7

- Make error_message nullable in DriveDeliveryStateChangeEntry

### 0.0.6

- Add DeliveryItemService APIs

### 0.0.5

- Add DeliveryDriveInfoService APIs

### 0.0.4

- Add DriveDeliveryStateChangeService APIs

### 0.0.3

- Add GetDriveOrderEntryBy... APIs

### 0.0.2

- Add client configs for Hermes
- Rename Item to Entry

### 0.0.1

- Add initial drive_order_service folder and files -- release.json, CHANGELOG.md
- Add `drive_order_service` to Makefile
- Add `drive_order.proto` with initial endpoints

