# Changelog for drive_protobuf

## In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

# 38.51.1
Add additional_amount_refunded_to_merchant to RefundResult

# 38.51.0
Add new returntype for pizza bag roundtrip

# 38.50.0
Add new ReturnDeliveryType for pizza bag return

# 38.49.5
Add lowerBoundQuoteDeliveryTime and upperBoundQuoteDeliveryTime to GetDeliveryResponseData

# 38.49.4
Add created_by to PreviewItemLevelRefundRequest

# 38.49.3
added lowerBoundQuoteDeliveryTime and upperBoundQuoteDeliveryTime to DriveEstimatesAPIResponse

# 38.49.2
Added source field to PreviewItemLevelRefundRequest

# 38.49.1
added event publish timestamp to UpdateGetDeliveryCacheRequest

# 38.49.0
Proxy CreateReturns in fulfillment gateway through Drive. This adds a new RPC endpoint to DriveReturnDeliveryService that allows creating return deliveries through Drive's interface rather than Dsher app calling fulfillment gateway directly as we need link redelivery in drive. 

# 38.48.6
Add DriveParcelsMerchantReportedParcelDimensions iguazu event

# 38.48.5
Update common and task-service versions

# 38.48.4
Add drive order id in request

# 38.48.3
Create Test Drive Order Service

# 38.48.1
Annotate Drive Cancellation Reasons Endpoint for UG

# 38.48.0
Add Drive Cancellation Info API

# 38.47.1
Add refund requester to DriveRefundResultData

# 38.47.0
added new drive fx event

# 38.46.0 
Add support for overrides to Drive Refunds API

# 38.45.0
Add expires_by in CreateDeliveryRequest

# 38.44.0 
Add new rpc endpoints for triggering drive order event handlers and update cache handlers

# 38.43.1
Added OrderRouteType and OrderRouteItem to DriveOrderResponse in public API

# 38.42.00
onboard DriveMiddlewareProviderService to UG

# 38.41.00
Add order UUID as an identifier to Drive tracking page protos

# 38.40.01
Update field type ShiftReceiptListViewPost

# 38.40.00
Add new function ShiftReceiptListViewPost

# 38.39.17
Refactor DriveRefundRejectionData to DriveRefundResultData

# 38.39.16
Added pizza bag to order route items

# 38.39.15
Register DriveRefundRejectionData iguazu event schema

# 38.39.6
Added refund_status and explanations to PreviewItemLevelRefundResponse and CreateItemLevelRefundResponse

# 38.39.5
Enable java_generic_services for refund_matrix

# 38.39.4
Added GetRefundMatrixRowById endpoint and added UG config to PreviewItemLevelRefund and CreateItemLevelRefund

# 38.39.3
Added disable_update to CreateOrUpdateStoreRequest

# 38.39.2

Add enum SigneeType to GetDasherFulfillmentConfigurationResponse

# 38.39.1

Add enum ProductSource and ProblemLevel to GetRefundMatrixRequest

# 38.39.0

Add new enum FilterType to GetRefundMatrixRequest and RefundMatrixRowMetadata to response

# 38.38.0

Add new enum value PRODUCT_SOURCE_DRIVE_SUPPORT_EMAIL_AUTOMATION to ProductSource enum

# 38.37.4

Add item details field to DriveOrderResponse

# 38.37.2

Add PinCodeVerificationDetails in GetOrderDetails to display on Mx portal

# 38.36.0

- Register DriveCancellationData iguazu event schema version bump

# 38.35.4

- Register DriveCancellationData iguazu event schema

# 38.35.3

- Adding ReturnDeliveryType to DriveOrderResponse

# 38.35.2

conflict resolution

# 38.35.1

Add a new enum UpdateItemsUseCase within UpdateItemsRequest

# 38.35.0

Add new fields in Item used in GetItemsWithSettings and UpdateItemsRequest for diagnostics orders

# 38.34.0

Add new fields to GetRefundMatrixResponse and annotate for unified-gateway

# 38.33.3

Add Parcel Route Id to CreateDeliveryRequest Drive Data

# 38.33.2

Add new product source for parcel redelivery tool

# 38.33.1

Support list of default dropoff locations for diagnostic orders

# 38.33.0

Add the required changes for Drive form - diagnostics lab order type

# 38.32.0

- Update DriveFeeComponentType enum to cover new options

# 38.31.1

- Version bump to retry build

# 38.31.0

- Add merchant_recommended_substitute_external_ids to SubstitutionPreferences

# 38.30.3

- Updating Version to 38.30.3

# 38.30.2

- Adding Phone Number to DriveSkippedPhoneNumberValidationData

# 38.30.1

- Adding DriveSkippedPhoneNumberValidationData

# 38.30.0

- skip unchanged set to true

# 38.29.0

- bump version

# 38.28.0

- Bump proto version

# 38.27.0

- Bump proto version

# 38.26.0

- Add/Update pin_code type name

# 38.25.0

- Adding customer field to estimates endpoint on v1

# 38.24.1

- add source type field to v1, olo, and drive order actions cancellation requests

# 38.24.0

- Update refund api to return refund status

# 38.23.0

- Update common dependency to 2.7.74

# 38.22.0

- Add is_parcel_business to dasher pay configuration response

# 38.21.0

- Add Refund requester for item level refund

# 38.20.1

- Add new `Cash` case to OrderRouteItem `enum`

# 38.20.0

- Add Refund requester

# 38.19.1

- Version bump

# 38.19.0

- Adding Event History to GetOrderTrackingDataResponse

# 38.18.0

- Update OrderContains to have tobacco, hemp and otc items

# 38.17.0

- Add new error code card declined

# 38.16.0

- Add isPhotoOnDeliveryEnabled to GetDasherFulfillmentConfigurationResponse

# 38.13.0

- Add DropoffVerificationMethodDetails underneath DropoffDetails

# 38.11.0

- Add Pin Code Verification Metadata in Create/Get Delivery

# 38.10.0

- Add Order Resolution Tool Product Source

# 38.9.3

- Add Puerto Rico configuration NetsuiteCustomForm

# 38.9.2

- Add Puerto Rico NetsuiteCustomForm and NetsuiteMarket

# 38.9.1

- Add submission_context to UpdateOrderTrackingDeliveryRequest

# 38.9.0

- Add AdjustmentSource to DriveOrderItem

# 38.8.1

- Add Puerto Rico to country code

# 38.8.0

- Add UpdateOrderTrackingDelivery endpoint

# 38.7.0

- Add Widget Type and Preset to CreateWidget API

# 38.6.0

- Add new fields for dropoff delivery instructions

# 38.5.0

- Add PickupVerificationMetadata to DriveOrderDispatchResponse

# 38.4.2

- Add OTC medication fields in Portal Api

# 38.4.1

- Add store country and state instead of address in Portal Api

# 38.4.0

- make order route item a list

# 38.3.2

- Add fee to RegulatoryFeeConfig

# 38.3.1

- Add order route type and items to DriveOrderResponse

# 38.3.0

- Add new params to support pharma for drive create delivery portal request

# 38.2.1

- Update show delivery type parameter in GetPortalConfigurationsForDriveFormResponse

# 38.2.0

- Add GetPortalConfigurationsForDriveForm and getDeliveryFulfillmentDetailsForPortalOrder

# 38.1.4

- Add regulatory_configs and deprecate dasher_regulatory_config

# 38.1.3

- Add order_cart_id to OrderAdjustmentsDriveEvent for Revenue Platform

# 38.1.2

- Add dasher_regulatory_config to MiddlewareProviderRecord

# 38.1.1

- Add is_allowed_for_partner_reward_reversal to RefundDetails

# 38.1.0

- Add delivery_correlation_id to DriveDropoffAddressData

# 38.0.2

- Add prediction_info to DeliveryEstimateInformation

# 38.0.1

- Update pay on delivery banner enum name

# 37.0.1

- Add new fields to SupportContactModules to support multiple support phone numbers being returned

# 37.0.0

- Add text fields to banner

# 36.13.4

- Add generic banner and banner group fields

# 36.13.3

- Add more fields to returnInfo to support the new return flow

# 36.13.2

- Expose billing related entity IDs in Configuration API's payment config response

# 36.13.1

- Add drive account id to business & store API contract

# 36.13.0

- Add a PickupComponentDetails component for tracking page

# 36.12.0

- Add order_type to CreateDeliveryRequest
-

# 36.11.2

- Add external delivery id in GetOrderTrackingDataResponse.Identifiers object

# 36.10.2

- Add PB changes for DSX tracking page updates

# 36.10.1

- Add McD order ready signal API

# 36.10.0

- Adding GetDeliveryTrackingPageUrl() endpoint in DrivePortalAPI

# 36.9.0

- Add workflow platform API

# 36.8.9

- Bump version to re-publish proto

# 36.8.8

- Bump version to re-publish proto

# 36.8.7

- Bump version to re-publish proto

# 36.8.6

- Define GetDeliveryAllergenItems call

# 36.8.5

- Added tracking number to tracking page APIs

# 36.8.4

- update CustomerTrackingInitialState to add a new field for signal tracking page to show a banner

# 36.8.3

- Version update bump due to compile error

# 36.8.2

- Version update bump

# 36.8.1

- Update orderContains to have pharmacy items and age restricted pharmacy items

# 36.8.0

- Update orderContains to list in Drive APIs and add ageRestrictedPharma

# 36.7.2

- Add auto_complete_dropoff_address id to DriveDropoffAddressData

# 36.7.1

- Update the GetGuestConsumerId rpc to fetch by urlCode

# 36.7.0

- Add UpdateExternalBusinessId API

# 36.6.0

- Add OnboardBusinessForWithholding Request and Response

# 36.5.1

- Add rpc to get consumer id by drive order id

# 36.5.0

- Added GetEventHistory endpoint.

# 36.2.1

- Fix nit in proto

# 36.2.0

- Added fields in RefundAmount and ProcessDeliveryLevelRefundResponse

# 36.1.6

- Added dropped items for partial cart in deliveryResponse

# 36.1.5

- Added tax to Drive DriveEstimatesAPIResponse and GetDeliveryResponseData

# 36.1.4

- Added metadata as a type.

# 36.1.3

- Renamed merchant website url.

# 36.1.2

- Added updates to update widget api.

# 36.1.1

- Added updates to name and url.

# 36.1.0

- Added UpdateWidgetStatus API

# 36.0.1

- Added PARCEL and SOCIAL_IMPACT to line of business enum

# 36.0.0

- Added driver tip details to utils and rearranged

# 35.1.0

- Added driver zero tip fields in drive_public_api

# 35.0.1

- Fix nit in proto
-

# 35.0.0

- Refactoring widget endpoints to include content type

# 34.7.1

- Changed no driver tip variable names

# 34.7.0

- Add endpoint for preview legacy bulk refunds

# 34.6.0

- add endpoints for widget operations: CreateAccount and PublishWidget

# 34.5.6

- Add refundRuleId to legacy drive refunds endpoint

# 34.5.5

- Change ParcelDetails to location instead of address for origin location

# 34.5.4

- common dependency update

# 34.5.3

- Add fields to the GetOrderTrackingDataResponse for the drive parcel Cx Tracking Page
-

# 34.5.2

- Fix bulk refund proto, add missing item amount to request and update transaction id type to string

# 34.5.1

- Add endpoint for bulk refunds with custom amount and add legacy bulk tool as product source

# 34.5.0

- add endpoints for widget operations: GetWidgets, GetWidgetById, CreateWidget and UpdateWidget

# 34.4.0

- add developer_id and external_business_id to onboardExistingMxBusiness

# 34.3.0

- add activation_method to mwp service

# 34.2.0

- add related_entity_type to configurations proto

# 34.1.3

- Add Drive Parcel Midmile OriginFacilityId and Delivery Item length width height to drive public API V1

# 34.1.2

- Update portal error codes for alcohol version

# 34.1.1

- Update portal error codes for alcohol

# 34.1.0

- Add portal error codes for alcohol

# 34.0.2

- Add DriveOrderItem to DriveEstimatesAPIRequest
- Add WEIGHT_BASED_FEE to DriveFeeComponentType

# 34.0.0

- Refactoring list business api

# 33.30.1

- Fixing stores api grpc response patterns

# 33.30.0

- Adding get store by mds id endpoint

# 33.29.6

- Add WITHHOLDING_COMMISSION_FEE_BACKFILL to transactionTypes

# 33.29.5

- Add is_delivery_returnable to DriveOrderResponse

# 33.29.3

- Add cancellation reason to CancelDeliveryRequest

# 33.29.2

- Creating special_instructions in CreateDeliveryRequest.deliveryItem

# 33.29.1

- Update validate request api input parameters

# 33.29.0

- Add promotion data proto for drive_promotions topic

# 33.28.1

- Add special_instructions to DriveOrderItem

# 33.25.0

- Add error codes in deal term configuration API responses

# 33.24.1

- Add rpc GetDeliveryItemBarcodeStatus to DriveFulfillmentService

# 33.24.0

- Update schema for request dropoff address and response dropoff address

# 33.23.1

- Add FinancialDetails to Cx Tracking GetOrderTrackingData endpoint

# 33.22.1

- Register schema for request dropoff address and response dropoff address

# 33.22.0

- Adding schema for request dropoff address and response dropoff address

# 33.21.1

- Add CustomLayoutSettings in CustomerTrackingInitialState endpoint.

# 33.21.0

- Adding external_store_id in Redelivery Request

# 33.20.0

- Use oneof in GetBusinessRequest

# 33.19.0

- Adding getDeveloperByBusinessId

# 33.18.0

- Adding userId to configurations API to enable authorization checks

# 33.17.3

- Adding new dasher_checkout_payment_method param to DriveOrderForDispatchResponse

# 33.17.2

- Added new entries to the FulfillmentTag proto in drive_utils.proto

# 33.17.1

- Updating DriveAccessControl namespace

# 33.17.0

- Adding catering contacts emails to drive_data.proto

# 33.16.0

- Add drive_access_control

# 33.15.5

- Added new fields to message Item in configuration.proto

# 33.15.4

- Added phone_number_components to Dasher object

# 33.15.3

- Add support details to response for CustomerTrackingInitialState

# 33.15.2

- Add drive_fulfillment_tags and customer_arrival_time to DriveOrderDispatchResponse

# 33.15.1

- Add store phone_number to CustomerTrackingInitialStateResponse

# 33.15.0

- Add AccountUpdateByMdsBusinessId endpoint to accounts

# 33.14.0

- Add GetDeveloperByUserId to drive_developer

# 33.13.5

- Add identifiers to CustomerTrackingInitialStateResponse

# 33.13.3

- Add generic services to drive_refund

# 33.13.2

- Update common dependency to 2.4.125 which includes tsproto support in common

# 33.13.1

- Add cobranding_logo_image_url to CustomerTrackingInitialState response

# 33.13.0

- Add relationship_description to GET API response

# 33.12.0

- Add external_business_id to drive V1 API

# 33.11.0

- Add new endpoint GetFulfillmentTags to DriveUtilsService

# 33.10.8

- Added relationship_type to GetDeliveryResponseData

# 33.10.7

- Added DeliveryFeeTaxRefund to ProcessDeliveryLevelRefundResponse

# 33.10.5

- Added source to CreateDeliveryLevelRefundRequest and CreateItemLevelRefundRequest

# 33.10.4

- Add GetDriveOrderByDriveOrderId endpoint.

# 33.10.3

- Added drive_delivery_fee_tax_refunded_to_merchant to RefundDetails.

# 33.10.2

- Add additional timestamps to GetOrderTrackingDataResponse
- Add phoneNumber field to CustomerTrackingInitialStateResponse
- Update common proto version dependency

# 33.10.1

- Add developer_id to DriveOrderResponse

# 33.10.0

- Add GetWebhookEventsFromDoordashIdRequest

# 33.9.9

- Add new ProductSource enum: PRODUCT_SOURCE_CUSTOMER_ORDER_TRACKING
- Add to drive portal GetOrderTrackingData endpoint
  - Add options flag to request
  - Add Identifiers to request
  - Add request submission context to request
  - Add LiveOrderDetails to response

# 33.9.8

- Added drive_account_id field in configuration api

# 33.9.6

- Added flag for voice payment memory

## 33.9.5

- Add admin gateway bulk tools to product source.

# 33.9.4

- Add redelivery properties + payment method uuid to dispatch drive order object

# 33.9.3

- Add OOPS protos

# 33.9.2

- Add v2 api to product source

# 33.9.1

- Add correlation ID to drive webhook event record proto

# 33.9.0

- Add NS ID to NS configuration request

# 33.8.1

- Fix typo for skip_authorization

# 33.8.0

- Add new fields to ProcessDeliveryLevelRefund

# 33.7.0

- Add requester_user_id to ChangeDeliveryToScheduledTimeRequest

# 33.6.6

- Add created_at_page_token to GetWebhookEventsFromExternalDeliveryIdRequest

# 33.6.5

- Remove force_partnership_creation flag in configuration_api and add partnership_ids in data contract

# 33.6.3

- Addding RPC to start cadence workflows in sandboxes environment

# 33.6.2

- Undo deprecate old DRF fields

# 33.6.1

- Updated business creation enum to support lemonade use case

# 33.6.0

- Add force partnership creation flag to create, update business APIs

# 33.5.0

- Add repeated geo based fee for dasher_regulatory_fees

# 33.4.5

- Remove driveAdmin java outer class

# 33.4.2

- Set Store API generic services true

# 33.4.1

- Add onboard existing Mx Store to Drive

# 33.3.4

- Update Portal CreateDelivery to accept a PaymentMethod CASH enum

# 33.3.1

- Revert data-types for developer-id and external-ids in biz store api

# 33.3.0

- Add outage event message for fod sink topic.

# 33.2.1

- Updated business and stores api proto to have developer-id and external-ids as optional fields.

# 33.2.0

- Add BlockDasher endpoint

# 33.1.2

- Add PRODUCT_SOURCE_MERCHANT_PORTAL to product source enums

# 33.1.1

- Added more error codes for portal create delivery error propagation.
  - Added REQUEST_PICKUP_PHONE_NUMBER

# 33.1.0

- Add support drive form onboarding in business api

# 33.0.0

- Remove developer api key create and get grpc

# 32.0.0

- Fixes should_remove_force_batch_uuid to be in the right place (in the public API)

# 31.7.4 (DO NOT USE)

- Added should_remove_force_batch_uuid (in the wrong place in drive_data)

# 31.7.3

- Added more error codes for portal create delivery error propagation.
  - Added ERROR_CODE_MISSING_PAYER_DETAILS
  - Added REQUEST_FIELD_SCHEDULING_WINDOWS

# 31.7.0

- Add is_parcel and hub_external_store_id in CreateDeliveryRequest

# 31.6.0

- Add support for Payment Methods and alcohol configs to stores proto, endpoint GetStoresByDoorstepStoreIds
- Add ProductSource enum: PRODUCT_SOURCE_MERCHANT_PORTAL_APP_LOAD

# 31.5.0

- Add confirmed_by_dasher to drive internal status (metadata for cx tracking page)

# 31.4.0

- Add should_collect_store_id, has_manhattan_addendum to mwp endpoint

# 31.3.1

- Added more error codes for portal create delivery error propagation.
  - Added ERROR_CODE_CASH_TOTAL_LESS_THAN_DRIVER_TIP_AND_FEE

# 31.3.0

- Add CreateRedelivery to drive portal API

# 31.2.0

- Add is_test_developer to mwp endpoint

# 31.1.0

- Added more error codes for portal create delivery error propagation.
  - Added ERROR_CODE_INVALID_PICKUP_TIME
  - Added ERROR_CODE_INVALID_DROPOFF_TIME
  - Added ERROR_CODE_INVALID_SCHEDULING_WINDOWS

# 31.0.0

- Update drive transaction type name

# 30.12.2

- Opt-out some grpc_error_code for Drive V1 API

# 30.12.1

- Add missing error codes for drive portal errors

# 30.12.0

- Calibrate DrivePublicApi, DrivePortalApi, OloApi circuit_breaker config

# 30.11.0

- Adding client_phone_number, external_store_ids to ExternalMetadata of B+S API

# 30.10.0

- Adding contract fields to Drive Middleware provider

# 30.9.3

- Changed error from RepositoryError to WebhookEventRecordError in webhook event record proto.

# 30.9.2

- Added more request fields and error codes for portal create delivery error propagation.
  - Added ERROR_CODE_INVALID_TIP_AMOUNT
  - Added ERROR_CODE_ALCOHOL_NOT_ALLOWED
  - Added ERROR_CODE_INVALID_CUSTOMER_NAME
  - Added ERROR_CODE_DUPLICATE_EXTERNAL_DELIVERY_ID
  - Added REQUEST_FIELD_CONSUMER_FIRST_NAME
  - Added REQUEST_FIELD_CONSUMER_LAST_NAME
  - Added REQUEST_FIELD_ALCOHOL
  - Added REQUEST_FIELD_CASH
  - Added REQUEST_EXTERNAL_DELIVERY_ID

# 30.9.1

Add new transaction type item/delivery_level_order_refund.

# 30.9.0

Added ErrorDetails to Public CreateDelivery Response Error.

# 30.8.3

- Add missing error codes for portal errors proto and common request fields
  - Add ERROR_CODE_INSUFFICIENT_DASHERS_TO_FULFILL_ORDER
  - Add ERROR_CODE_NUM_ITEMS_TOO_LOW
  - Add ERROR_CODE_MAX_NUM_ITEMS_EXCEEDED
  - Add ERROR_CODE_INACTIVE_STORE
  - Add ERROR_CODE_DRIVE_NOT_CONFIGURED_FOR_STORE
  - Add ERROR_CODE_DRIVE_PARTNERSHIP_NOT_CONFIGURED_FOR_STORE
  - Add ERROR_CODE_INVALID_PHONE_NUMBER
  - Add REQUEST_FIELD_NUM_ITEMS

# 30.8.2

- Change parameters in webhook event record

# 30.8.1

- Add CREATE_DEVELOPER_ERROR_CODE_CREATION_FAILED_CX_FAULT

# 30.8.0

- Add get webhook events by developer id

# 30.7.0

- Add rank to drive MWP Short record

# 30.6.0

- Add error response in delivery receipt list view post response

# 30.5.1

- Add new endpoint GetCaseAndConsumerByContactId

# 30.5.0

- Add minimum_order_threshold_cents to CreateDealTermConfigurationRequest

# 30.4.0

- Add ErrorDetails data to generic error response object

# 30.3.0

- Add WebhookEventRecord proto

# 30.2.0

- Add Drive MWP Service

# 30.1.0

- Add generic RequestField enum to describe request fields in any drive endpoints for error responses
- Add REQUIRED_FIELD, ORDER_SUBTOTAL_TOO_LOW, and ORDER_SUBTOTAL_EXCEEDS_LIMIT error codes for portal
- Add map<string, string> metadata to drive_data proto object: Error so endpoints can optionally provide metadata when an error occurs

# 30.0.0

- Rename pagination token to continuation token

# 29.2.0

- Add dasher id in delivery receipt list view post response

# 29.1.0

- Add error codes to deal term config response

# 29.0.0

- Add delivery receipt list view post proto contracts

# 28.1.0

- Add developer to GetOrderTrackingDataResponse

# 28.0.0

- Add dasher regulatory fee fields to deal term request

# 27.0.0

- Changing store status to an enum

# 26.0.0

- Added SchedulingDetails to Portal CreateDelivery

# 25.2.2

- removing isTest from stores/business proto contracts

# 25.2.1

- Fixing bugs with stores/business proto contracts

# 25.2.0

- Add StaticApiKey Create & Get

# 25.1.0

- Add dasher_dynamic_instructions to StoreAddressLinkResponse

---

# 25.0.0

- Add DriveOrderItem and RequestSubmissionContext to Portal CreateDeliveryRequest
- Add Address type in CreateDeliveryRequest

# 24.6.0

- Add Drive Order timeliness, fulfillment funnel, fees aggregation models

# 24.5.0

- Add GetBusinessByDeveloperId

# 24.4.0

- Update DriveAPI enum with a new API - MARK_ORDER_READY_FOR_PICKUP_STATIC

# 24.3.0

- Add external business id and developer id support

# 24.2.0

- Add locale field to UserSubmitContext object

# 24.1.1

- Update attributes in ExternalMetadata object to be nullable

# 24.1.0

- Updated datatypes for business store api

# 24.0.1

- Add new product source enum DRIVE_PUBLIC_API_V1 for the ProductSubmitContext object

# 24.0.0

- Update status code from error code for configurations api

# 23.53.0

- Add is_test flag to DeveloperV1Request

# 23.52.0

- Add Drive Portal CreateDelivery contract

# 23.51.0

- Add return fee fields to CreateDealTermConfigurationRequest

# 23.50.0

- Add CreateDeliverySimulator to drive_data.proto

# 23.50.0

- Set generic java service config to true in StoresService

# 23.49.1

- Updated product source in request submission context object.

# 23.49.0

- Add delivery creation status to drive order response

# 23.48.0

- Add request submission context object
- Apply usage of new object RequestSubmissionContext object in the Drive Portal GetDeliveryEstimatesRequest/endpoint

# 23.47.2

- Add Store ID as part of Configurations API

# 23.47.1

- Fix typo in GetDeliveryEstimates endpoint - rename field to correct spelling of "identifier"

# 23.47.0

- More required fields for get delivery serializer
- Remove non-used fields added

# 23.46.0

- Add Drive Portal GetDeliveryEstimates contract
- Add Drive Portal error codes

# 23.45.1

- add ignore PACKAGE_VERSION_SUFFIX back for business api

# 23.45.0

- Update Netsuite Fields for New Zealand

# 23.44.0

- Fulfillment configuration changes

# 23.43.6

- Update business proto api

# 23.43.4

- Adding store proto api contracts

# 23.43.2

- Tweaking business rpc contracts

# 23.43.1

- Adding payment method to the Configuration Payment Request

# 23.43.0

- Adding allow_unattended_delivery field to DriveOrderResponse

# 23.42.0

- Fixing business input for admin business contracts.

# 23.41.2

- Added new drive admin business contracts.

# 23.41.1

- Add Payment methods to Create Configuration API

# 23.41.0

- Add Deal terms to Create Configuration API

# 23.40.1

- Register proto

# 23.40.0

- Add fulfillment event

# 23.39.0

- Add storefront flag to GetDasherLocationRequest

# 23.38.0

- Add storefront flag to GetOrderTrackingDataRequest

# 23.37.0

- Add downtime by 10% threshold, attribution fields to DriveAPIAggregatedStatsEvent

# 23.36.0

- Add auth protocol and extra header info in webhook config apis

# 23.35.1

- Add auth protocol and extra header info in webhook config apis

# 23.35.0

- OLO Accept Quote change to support right alcohol flag

# 23.33.0

- Add session id and external_delivery_id to estimates

# 23.32.0

- Adding ReturnInfo to configuration resp

# 23.31.1

- Change AutomateDeliveryLevelRefund to ProcessDeliveryLevelRefund
- Update some field naming and types for ProcessDeliveryLevelRefund endpoint

# 23.31.0

- Change contract for GetRefundsByDeliveryId to just GetRefunds

# 23.30.1

- Add refund_status to RefundResult

# 23.30.0

- Add automate refund endpoint
- Add reason code and reason comments code to GetRefundsByDeliveryId response. This is a backwards incompatible change to GetRefundsByDeliveryId because we change the refund_details type, but the method is unimplemented, so it's safe.

# 23.29.0

- Adding dynamic_delivery_time to MetaData

# 23.28.1

- Add payment_method to DriveOrderResponse.

# 23.28.0

- Added retry option to PostCateringVerification

# 23.27.0

- Added DriveGoldenGrpcAPI for golden project.

# 23.26.0

- Fixing a few incorrectly placed fields.

# 23.25.1

- Added new drive APIs in bifrost for MCD.

# 23.25.0

- Added barcode_scanning_required, num_items, items, order_volume
  to UpdateDeliveryRequest

# 23.24.0

- Added the return info and other fields to the Drive configuration service

# 23.23.0

- Added the proto service method to update delivery items.

# 23.22.1

- Add is_inkind_delivery to OrderPlacedDriveEvent.

# 23.22.0

- Add delivery_id to GetDeliveryResponseInternalData and add GetDeliveryResponseInternalData to GetDeliveryResponse

# 23.21.0

- Add MerchantEquipped/Unenquipped Pizza bag

# 23.20.0

- Add dasher id to PostCateringVerificationRequest

# 23.19.0

- Add equip_dx_for to fulfillment configuration

# 23.18.0

- Add GetOrderTrackingData endpoint

# 23.17.1

- Added fee_breakdown to Drive DriveEstimatesAPIResponse

# 23.17.0

- Added fee_breakdown to Drive GetDeliveryResponseData

# 23.16.0

- Add is_withholding_merchant to the DriveOrderDispatchResponse

# 23.15.0

- Add pickup_verification_image_url to the GetDeliveryResponseData

# 23.14.1

- Added locale and tax rate to invoicing group

# 23.14.0

- Add external_delivery_id to UpdateDeliveryRequest

# 23.13.0

- Add includeDriveAccount option flag for GetStoresByDoorstepStoreIds endpoint

# 23.12.0

- Add invoicing_group_id to DriveOrderDispatchResponse message

# 23.11.0

- Add downtime, avg latency fields to DriveAPIAggregatedStatsEvent

# 23.10.0

- Added the proto contract for itemsWithSettings

# 23.9.1

- Add DriveAPIAggregatedStatsEvent to register_schema

# 23.8.0

- Add POST Catering Verification RPC and Request

# 23.7.0

- Add Bifrost Drive aggregated API events protos

# 23.6.1

- Add contains_alcohol to OLO accept quote request

# 23.6.0

- Add external_store_id to OLO requests

# 23.5.0

- Add catering verification id on GetCateringVerificationByDeliveryIdResponse

# 23.4.2

- Bump to regenerate tsproto files, since compilation code changed.

# 23.4.1

- Add tsproto to list of supported languages.

# 23.4.0

- Add is_p2p flag to DeliveryResponse for peer to peer deliveries.

# 23.3.0

- Add generate presigned url and create store catering setup instructions endpoint.

# 23.2.0

- Add DriveReturnType for CreateReturnDeliveryByDeliveryId

# 23.1.0

- Add new return delivery endpoints

# 23.0.0

- Fix the setup_pay_eligible on dasher fulfillment config api

# 22.4.1

- Add transaction amount and transaction tax to transactionAmountType

# 22.4.0

- Added more fulfillment config fields

# 22.3.0

- Added the catering setup instructions

# 22.2.0

- Update merchant payment adjustment proxy

# 22.1.0

- Added items to the DasherFulfillmentConfiguration

# 22.0.0

- Update Address type in dropoff details in drive_order_actions

# 21.9.0

- Add support to query Drive Partnerships and CateringInstructions in GetBusinessConfiguration API:
  - Add option in request to set new flag: includeDrivePartnerships
  - Add option in request to set new flag: includeCateringSetupInstructions
  - Add DrivePartnershipDetails object in response in order to return a list of DrivePartnerships
  - Add CateringSetupInstructions object in response in order to return catering instructions

# 21.8.0

- Add merchant payment adjustment proxy

# 21.6.0

- Add GetDriveOrderByUrlCode under drive_order

# 21.5.0

- Add UpdateDelivery under drive_order_actions

# 21.4.0

- Add GetStoresByDoorstepStoreIds, and add few fields to StoreResponse.

# 21.3.1

- Adds shopping_required to get delivery contract

# 21.3.0

- Add consumer_address_link parameters for CreateDriveGuestConsumer

# 21.2.0

- Add legacy CreateDriveGuestConsumer endpoint

# 21.1.0

- Add a new service drive order actions. Adding an endpoint cancel delivery

# 21.0.0

- Get Payment Card by Developer

# 20.0.0

- Remove OUTAGE_REFUND TransactionType

# 19.6.1

- Add OUTAGE_REFUND TransactionType

# 19.6.0

- Add NZ country code and currency

# 19.5.0

- Add DSJ endpoints to trigger cancellation tasks

# 19.4.1

- Add card on developer. Create invalid Uuid error code

# 19.4.0

- Create Add card on developer

# 19.3.1

- Add the Outage MatrixEntityType

# 19.3.0

- Add GetDriveOrderByDoorDashId endpoint to DriveOrderAPI

# 19.2.2

- Add LineOfBusiness enum to RefundMatrixRow

# 19.2.1

- Add stripe customer id to store object

# 19.2.0

- Add multiple onboarding rules to GetInvoicingGroupOnboardingRuleByDoorstepId endpoint

# 19.1.0

- Add create_return_delivery endpoint

# 19.0.0

- Move catering verification to separate endpoint

# 18.15.0

- Add line_of_business in DriveOrderDispatchResponse

# 18.14.0

- Adding setup_pay verification details to getDasherFulfillment

# 18.11.2

- Adding Japan and Germany currencies and countries

# 18.10.2

- Add promotion_id to public api requests

# 18.10.1

- Add developer_id to DriveOrderForDispatch response

# 18.10.0

- Adding customer locale optional input

# 18.9.0

- Moved incorrect gRPC fields in DriveOrder to correct location

# 18.8.0

- Add shopping_required to CreateDelivery and shopping_config to DriveOrder

# 18.7.0

- Quote accept pass in optional requested times

# 18.6.0

- Add api for updating drive order scheduled time

# 18.5.0

- GetDeveloper API to support filter by integration_type and is_test

# 18.4.0

- Add an endpoint to get developer info using doorstep business id

# 18.3.0

- Add an endpoint to get internal delivery id using external delivery id for Developer Service's Delivery Simulator

# 18.2.2

- Add webhook config APIs

# 18.2.1

# 18.2.0

- Add GetDeliveryVerificationEndpoint

# 18.1.0

- Add get invoicing group membership by doorstep store id

# 18.0.1

- Add reasons_for_deactivation_string_value to InvoicingGroup

# 18.0.0

- Make stripeCardToken nullable drive_developer

# 17.2.0

- Add optional full address field

# 17.1.0

- Fix response for iguazu proxy event

# 17.0.0

- Make stripeCardToken non-null drive_developer

# 16.0.0

- Make stripeCardToken non-null

# 15.10.0

- Add stripeCardToken to createStore v2

# 15.9.0

- Proxy Quotes Event from DSJ to Drive

# 15.8.1

- Add pickupBusinessName to DriveOrderDispatchResponse

# 15.8.0

- Add stripeCardToken to createDeveloper v2

# 15.7.0

- Add invoicing group onboarding rule endpoint

# 15.6.2

- Bump the pipeline, 15.6.1 never published.

# 15.6.1

- Add DriveTransactions to DriveOrderDispatchResponse

# 15.6.0

- Add DSJ service endpoint to onboard store for invoicing

# 15.5.1

- Add quoted_pickup_time and quoted_delivery_time to DriveOrderDispatchResponse

# 15.5.0

- Add external_delivery_id to CancelDeliveryRequest

# 15.4.0

- Add Store AOR features

# 15.3.0

- Add new promotion campaign types

# 15.2.2

- Add developer_uuid to GetDoordashIdByExternalDeliveryIdRequest

# 15.2.1

- Change reasons_for_deactivation in InvoicingGroup from Enum to list of String

# 15.2.0

- Add new fields is_grocery and is_retail on DriveOrderDispatchResponse

# 15.1.0

- Adding new flag in dasher fulfillment config to control show contact Cx steps in dasher mobile.

# 15.0.0

- Rewrite createDeveloper v2 grpc arguments

# 14.2.0

- Return order_uuid in OrderCartResponse

# 14.1.1

- Add starting_point_id to CreateDeliveryRequest

# 14.1.0

- Adding createDeveloper v2 endpoint drive_developer.proto

# 14.0.1

- Add isTest flag to work with developer_uuid in public API

# 14.0.0

- Rewriting createDeveloper v1 endpoint drive_developer.proto

# 13.2.2

- Add status and reasons_for_deactivation for invoicing_group/common.proto

# 13.2.1

- Try to make DeveloperApiService generate a service file

# 13.2.0

- Add GetDeveloper endpoint in drive_developer.proto

# 13.1.0

- Remove marked deprecation on SaaS refund fields

# 13.0.1

- Add errors to DriveDeliveryDetails API

# 13.0.0

- Add subtotal field to DriveOrderDispatchResponse
- Change drive_order_id to Int64Value

# 12.6.2

- Reuse DriveFees in DriveDeliveryDetails API

# 12.6.1

- Modify error code names in DriveDeliveryDetails API

# 12.6.0

- Modify quote accept error response to indicate field validation error

# 12.4.0

- Adding drive order id to refund transactions details model
- Deprecating delivery ID field

# 12.3.1

- Add column delivery_id in DriveOrderResponse

# 12.3.0

- Added many fields to DriveOrderDispatchResponse in drive_protobuf/drive_order.proto

# 12.2.0

- Rewriting create developer proto contract

# 12.1.0

- Adding the rpc method for check addresses endpoint

# 12.0.1

- Add suspected for fraud to deactivation reasons

# 12.0.0

- More changes for API rollout

# 11.0.0

- Change TrtAdjustment transaction_id (unused field) type from int64 to stringvalue

# 10.2.1

- Adding contract for drive developer onboarding contract/response in drive_developer.proto

# 10.2.0

- Added model definitions for BusinessConfigurationRequest/BusinessConfigurationResponse in drive_portal_api.proto

# 10.1.1

- Add transaction_id to trt adjustment drive event

# 10.1.0

- Add model definitions for GetDasherPhoneNumber in drive_portal_api.proto

# 10.0.0

- Change type of refund type in RefundDetails object to enum

# 9.2.0

- Add is_delivery_returnable to DriveOrderDispatchResponse

# 9.1.1

- Adding developer_uuid for public api

# 9.1.0

- Adding refund matrix endpoints to get the matrix

# 9.0.0

- Change int64 to Int64Value

# 8.0.0

- New preview refund APIs
- Adjust create APIs to require less information

# 7.8.2

- Add id to DriveOrderItem
- Add is_cold_chain, store_payout_total, store_payout_total_no_errors to DriveOrderDispatchResponse

# 7.8.1

- Adding invoiced_at for trt adustment to RP

# 7.8.0

- Adding new fields to Estimate API to support BatchEstimates

# 7.7.0

- Add new transaction types

# 7.6.0

- Add 6 new fields to DriveOrderResponse:
  - num_items
  - order_value
  - tip
  - commission_tax
  - quoted_pickup_time
  - quoted_delivery_time

# 7.5.1

- Add javascript support to drive_protobuf

# 7.5.0

- New DriveRefund endpoints

# 7.4.6

- Add order_volume_scalar_source to dasher fulfillment configuration endpoint

# 7.4.5

- Add order_volume_classification to dasher fulfillment configuration endpoint

# 7.4.4

- Add external_id and barcode to DriveOrderItem

# 7.4.3

- add store deactivation status and reasons for deactivation enum

# 7.4.2

- Rename GetDriveOrderForDispatchByDeliveryId to GetDriveOrderForDispatch

# 7.4.1

- Add changes required for item-level refunds for Support as a Service from Drive

# 7.4.0

- Add google_place_id to Address

# 7.3.0

- Change CreateDeliveryResponse proto

# 7.2.8

- adding google_place_id to Address

# 7.2.7

- adding post_tip to DriveOrderResponse for dasher pay calculation

# 7.2.6

- adding is_from_non_tip_merchant to GetDasherPayConfigurationResponse

# 7.2.5

- adding get priority ranked SaaS config endpoint

# 7.1.5

- adding acceptance_rate_fee_adjustment to transaction_type

# 7.1.4

- adding trip_id to GetDeliveryEstimateRequest

# 7.1.2

- changing some primitive types to Google Protbuf types to allow null values
- add "none" value to ContactType to represent null

# 7.1.1

- changing entity id type to int64 in Get Request for consistency with Create

# 7.1.0

- adding update endpoint to SaaS Config APIs
- get result not repeated Saas Config

# 7.0.2

- Add error field in OloApi.CancelDelivery

# 7.0.1

- patch to return single saas config instead of list

# 7.0.0

- changing structure of request of SupportAsAServiceCreateRequest

# 6.23.0

- add support as a service config endpoint

# 6.22.2

- Add optional price field to DriveOrderItem

# 6.22.1

- Add error field for drive order GetDoordashIdByExternalDeliveryIdResponse

# 6.22.0

- Replace doordash_id with external_delivery_id in OloApi.CancelDelivery

# 6.20.0

- Add missing data columns in drive quotes events

# 6.19.0

- Add create delivery endpoint

# 6.18.0

- Add missing data in get_delivery_estimate for event publishing

# 6.17.0

- Add unified api bifrost proto for all drive delivery api events

# 6.16.0

- Add get store tax rate in drive_data

# 6.15.2

- Add request path to drive quoted estimates data

# 6.15.1

- Add developer_id to drive quoted estimates data

# 6.15.0

- Data schema for unifying drive order estimates data and drive quote data

# 6.13.0

- Add quoted_delivery_time to CreateAndSaveEtaPrediction endpoint

# 6.12.0

- Add OLO bifrost API event protos

# 6.11.0

- Add CancelDelivery to OLO API

# 6.10.0

- Add validate, get, update, cancel delivery bifrost API events

# 6.9.4

- Add external_business_name(brand_name) to drive_order GetDoordashIdByExternalDeliveryIdRequest

# 6.9.2

- Add adding DriveWebhookService::SendWebhooksForParkingDetails, removing DriveWebhookService::TriggerWebhooksForDeliveryEvents

# 6.9.0

- Add store_id, business_id, business_name to DriveEstimatesResponse

# 6.8.1

- Adding events for bifrost tracking

# 6.7.2

- Add promotion_applies_to_regulatory_fees in drive_estimate_response

# 6.7.0

- Add field errors to OLO get quote

# 6.6.3

- Add external_store_id as optional field in drive_order request

# 6.6.2

- Add payment_account_id field in InvoicingGroup

# 6.6.1

- Add store_id as optional field in drive_order request

# 6.6.0

- Added updateMethod to PartnershipCreateRequest

# 6.5.2

- Add Cancellation adjustment to drive transaction type enum

# 6.5.1

- Add Commission adjustment to drive transaction type enum

# 6.4.2

- Add Cancellation to drive transaction type enum

# 6.4.1

- Add Commission adjustment to drive transaction type enum

# 6.4.0

- Add external_pickup_zone_id to drive_order response

# 6.3.2

- Additional correction of types for DeliveryEstimationInformation segment message

# 6.3.1

- Correct types for DeliveryEstimationInformation segment message

# 6.3.0

- added GetServiceArea to OLO API

# 6.2.1

- move GetDoordashIdByExternalDeliveryId to drive_order

# 6.2.0

- Add dasher action confirmation fields to Dasher in drive_public_api

# 6.1.4

- minor change DoorDash to Doordash in drive_data

# 6.1.2

- Fix the spelling problem in drive transaction type

# 6.1.1

- Move GetDoorDashIdByExternalDeliveryId to drive_data

# 6.1.0

- Added GetDeliveryIdByExternalDeliveryId to drive_public_api

# 6.0.3

- Fixed typos with Segment DeliveryEstimationInformation

# 6.0.2

- Fixed by removing fields that belong to post-delivery-creation

# 6.0.1

- Fixed the driver_reference_tag naming and timestamp type in DeliveryEstimateInformation

# 6.0.0

- Added missing fields to DeliveryEstimateInformation in SubmitDeliveryRequest and drive_segmen

## 5.6.0

- Added type to Vehicle in drive_public_api

## 5.5.1

- Added dasher wait time discount and tip rate discount to drive transaction type

## 5.5.0

- Added quote_id to DeliveryEstimationInformation

## 5.4.0

- Added quote_id to DeliveryEstimateResponse

## 5.2.1

- Added some new BusinessPaymentOnboardingErrorCode exceptions

## 5.2.0

- Added the iguazu event proto for drive quotes

## 5.1.1

- add events subfolder in manifest.in

## 5.1.0

- Add post_tip_amount to DsjPostTipDriveEvent message

## 5.0.0

- Make BusinessUnification and StoreUnification primary IDs nullable

## 4.0.3

- Add Customer details to GetDriveOrderByDeliveryId

## 4.0.2

- Adds configuration namespace to manifest.in

## 4.0.1

- Adds dasher_locale to dasher fulfillment configuration endpoint

## 4.0.0

- Adds combined special instructions to dasher fulfillment config endpoint
- Adds delivery id as a required prop to dasher fulfillment config endpoint (BREAKING)

## 3.25.0

- AddDriveOrderToPendingCache endpoint for delivery creation fallback

## 3.24.0

- Add optional order_ready_time field to CreateDeliveryRequest

## 3.23.0

- Add BusinessUnification and StoreUnification segment events

## 3.22.0

- Add payment onboarding for business (get or create invoicing group, onboarding rule, netsuite entity)

## 3.21.0

- Add a map of additional fields to be added to Drive Partnerships onboarded through SFDC

## 3.20.0

- Add dasher regulatory fees to GetDeliveryEstimate response

## 3.19.0

- Add doordash_id param to GetDriveOrderByDeliveryId response

## 3.18.0

- Modify drive catering setup instructions naming instructions_url for drive portal API

## 3.17.0

- Add is_from_store_to_us and super_category to OrderPlacedDriveEvent
- add revenue_platform.proto to .pullapproval.yml

## 3.16.0

- Add external_delivery_id param to GetDriveOrderByDeliveryId response

## 3.15.0

- Add DriveEvent wrapper and enum of eventtypesfor revenue platform consumption
- Made typo fix

## 3.14.0

- Updates to SFDC Extraction end-point
  - add error messages to response
  - update types
  - add missing values

## 3.13.0

- Add CancelDelivery endpoint on DSJ

## 3.12.4 (do not use 3.12.2, 3.12.3 is unknown since this file wasn't updated)

- Adds delivery_id param to getdasherpayconfiguration endpoint

## 3.12.1

- Adds is_contactless_delivery to DriveOrder

## 3.12.0

- Add GetOrCreateOrderCart to DSJ for submit delivery extraction

## 3.11.1

- Add java_generic_services for Hermes support

## 3.11.0

- Add all transaction types from the drive transaction table to transactionTypes

## 3.10.0

- Change naming convention of transactionAmount to transactionAmountType
- Add seperate field for transactoinAmount

## 3.9.0

- Add DriveTransaction to drive_transacton.proto

## 3.8.2

- Adds missing pickup instructions field to drive config endpoint

## 3.8.1

- Removes unnecessary config fields

## 3.8.0

- Add Create Partnership endpoint for SFDC Extraction

## 3.7.0

- Add endpoint for creating partnerships from salesforce opportunity

## 3.6.0 and 3.6.1

- (3.6.0) Add configuration endpoint for the dasher bff's get delivery functionality
- (3.6.1) Renames the endpoint for clarity (no clients using this yet, so not breaking anything)

## 3.4.0

- Add revenue_platform.proto and new event directory
- Add OrderPlacedDriveEvent to revenue_platform.proto
- Add PostTipDriveEvent to revenue_platform.proto
- Add OrderAdjustmentsDriveEvent to revenue_platform.proto
- Add TrtAdustmentDriveEvent to revenue_platform.proto
- Add DsjPostTipDriveEvent to revenue_platform.proto
- Add DriveFees to drive_protobuf/common.proto
- Add ReturnType to drive_protobuf/common.proto
- previous sha for the above change e1c9bcff3787370bad169a6d3446c9b2d4f7aa37

## 3.3.1

- Add FULLY_APPLIED to NetsuiteRecordStatus
- Add errors to StoreOnboardingErrorCode

## 3.3.0

- Add TIP_ADJUSTMENT as a Drive Transaction Type

## 3.2.0

- Add endpoint for creating partnerships, with child logic

### UNKNOWN

- Didn't increment changelog :(

### 3.0.0

- Forced by linting to combine packages in tasks into a single package
- Add CountryCode to drive_protobuf/common.proto
- Add country and driveAccountId to InvoicingGroupCreateRequest
- Create new invoicing_api/OnboardNewStore endpoint
- Create new invoicing_api/GetMembershipByStoreId endpoint

### UNKOWN

- I guess we forgot to increment changelog for many versions....

### 0.6.4

- Added DASHER_REGULATORY_FEE as a type for drive_transaction

### 0.6.3

- Added new endpoint to refund a delivery

### 0.6.2

- Added user to GetInvoicesByBusinessIdRequest

### 0.6.0

- Added the invoice api

### 0.5.2

- Updated models for the delivery search portal api

### 0.5.0

- Added the delivery search portal api

### 0.4.0

- [Create `enum PaymentTerm` and add it to `InvoicingGroupCreateRequest`](https://github.com/doordash/services-protobuf/pull/2383)
