# Changelog for merchant-order-service

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

---
### 0.1.68
Add ASYNC PLATORM to ClientSource enum for UpsertBusyKitchenInfo endpoint

### 0.1.67
Add mds_org_id to updateFeatureConfig request. Necessary for updating provider feature configs.

### 0.1.66
Add LOM Plugin feature configuration endpoints

### 0.1.65
Bump common to 2.9.6

### 0.1.64
Add client source field to UpsertBusyKitchenInfo endpoint

### 0.1.63
Use Cx Hospitality field definition from common/mx_hospitality

### 0.1.62
Add new fields for Cx Hospitality Info to CustomerDetail

### 0.1.31
Add ended reason in TwilioStudioEventsWebhooksRequest

### 0.1.30
Update comment for ITEM_UPDATE in adjustOrder

### 0.1.29
Add ITEM_UPDATE in adjustOrder

### 0.1.28
Add query param for GetMenuItemExtraOptions

### 0.1.26
- Add query param to menu endpoint

### 0.1.24
- Add menu_item_extra_option_id in GetOrdersDetail

### 0.1.16
- Add query param to menu GetItemExtras

### 0.1.16
- new notification event types: consumer pickup and revert picked up status

### 0.1.15
- Add new rpc for tablet calling

### 0.1.10
- adding new entit type delivery

### 0.1.9
- add send notification timestamp
- 
### 0.1.5
- Add new rpc for studio events

### 0.1.1
- New endpoint AdjustOrder

### 0.0.8
- Add batch_id to order response for batch orders

### 0.0.7
- Add new rpc getActiveOrders in merchant-order-service.
- Add new rpc getOrdersDetail in merchant-order-service.

### 0.0.5
- new grpc service and adding push notification

### 0.0.4

- new rpc connect participants.

### 0.0.3

- Define menu API contracts.

### 0.0.1

- Initial proto set up for merchant-order-service
- Add `merchant-order-service` to Makefile
