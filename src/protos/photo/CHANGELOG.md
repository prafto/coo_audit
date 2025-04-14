Changelog for photo

### In `release.json`, increment the tag like so:

### Given a version number MAJOR.MINOR.PATCH, increment the:

1. MAJOR version when you make incompatible API changes,
2. MINOR version when you add functionality in a backwards-compatible manner, and
3. PATCH version when you make backwards compatible bug fixes.

## 0.2.85
- Add business id and photo name to photo proto

## 0.2.83
- Add rpc for request a review

## 0.2.82
- Add EmailNotification WF manual trigger

## 0.2.76
- Add new use case to PhotoUseCase: Dx profile photo

## 0.2.71
- Add moderatorId and client to ApprovePhotoVariant APIs

## 0.2.67
- Add moderatorId to Approve/RejectPhoto APIs

## 0.2.63
- Add Crud Rpcs to FlashMod

## 0.2.60
- Enable multi-select use-case for moderation

## 0.2.56
- Add new use case to PhotoUseCase: Cx profile photo

## 0.2.49
- Add reingest parameter to the ReUploadPhoto API

## 0.2.46
- Add reingest override to ProcessCnGPhoto API

## 0.2.43
- Add status to ProcessCnGPhotoResponse

## 0.2.42
- Add start notification workflow rpc

## 0.2.41
- Add photoOperation's operation as a string

## 0.2.40
- Add notification gateway

## 0.2.37
- Add auto_linked_at and auto_approved_at to photo metadata

## 0.2.32
- Add use case PHOTO_USE_CASE_CNG_CHECKOUT_RECEIPT

## 0.2.31
- Update CreateAndUploadPhotoVariantResponse to return PhotoEntity

## 0.2.30
- Add GetSignedImageUrl to PhotoServingGateway

## 0.2.29
- Add origin_photo_id to CreateAndUploadPhotoVariantResponse

## 0.2.28
- Add comments and created_by_id to ApprovePhotoVariantRequest

## 0.2.26
- Add new endpoint - AutoReviewSafetyPhoto

## 0.2.25
- Add use case PHOTO_USE_CASE_THQ

## 0.2.25
- Add is_variant to photo meta

## 0.2.24
- Add two new rpcs for moderator rescues
  - Create and upload a photo variant
  - Approve a photo variant

## 0.2.23
- Add ApprovePhotoVariant rpc to approve photo variant

## 0.2.20
- Change the photoValidation status from enum to responseCode 

## 0.2.18
- Add file_date to StartYelpProcessWorkflowRequest so we can trigger the workflow for a specific date

## 0.2.17
- Add two new rpcs for photo validation. The rpcs are
  - Get total count of photos in a timeframe (getTotalPhotosByTimestamp)
  - Get photo records within a timeframe using limit and offset (getPhotosByTimestampWithLimitAndOffset)

--
## 0.2.16
- Add a new endpoint to manually trigger yelp workflow

--
## 0.2.15
- The RPC is not live. Moving to photoReviewingGateway makes more sense
since PDS is usually used for CRUD operations

--
## 0.2.14
- Update ver. to republish proto to artifactory

## 0.2.13
- Add rpc for starting photoOperation workflows

--
## 0.2.12
- Add validation status to meta field for detecting broken photos


--
## 0.2.11
- Reset the photo expires_at field to be Long

--
## 0.2.9
- Add Salient Rect to photo metadata

--
## 0.2.8
- Update the photo expires_at field to be Timestamp

--
## 0.2.7
- Add expires_at to the Photo proto
- Add expiration_time to CreateAndUploadPhotoFromUrlRequest

--
## 0.2.6
- Update PhotoUseCase to include new DINE_OUT use_case

## 0.2.5
- Update PhotoUseCase to include new DASH_CHAT use_case

--
## 0.2.4
- updates createAndUploadPhoto endpoint to take additional auto_review_photo to determine whether or not to run the
auto_qa on the photo

--
## 0.2.3
- adds the new create and upload photo from url endpoint request and response protos

--
## 0.2.2
- Update PhotoUseCase to include new YELP use_case

--
## 0.2.0
- Update RejectPhotoRequest to include comments and created_by to prevent rejecting photos without feedback

--
## 0.1.9
- Add a new set of protos for the auto_review cadence workflow including: GoogleVisionFeatureType, auto_rejected_at

## 0.1.6
- We are now populating the originalContentHash field. Since we have an index built on this endpoint
we can retrieve this photo in the photoDataService layer. Will include the serving layer once we
expose the endpoint.

## 0.1.5
- Add drive and bulk service in photo use case and add photo_use_case parameter to processCnGPhotoRequest

## 0.1.4
- dummy pr to bump up version 

## 0.1.3
- Add the width, height, and size fields to the photoMeta proto field to include dimension metadata in
photo DB.

## 0.0.68
- Add API's to submit UGC Photos for moderation to become eligible for Menu Display.

## 0.0.66
- CreateAndUploadPhoto is now serving Credits and Refund(CNR) traffic, so we will need additional use case.

## 0.0.65
- Add additional message fields to allow for more advanced filtering for deleting photo moderations
- Add getPhotoModerationsByUuid rpc that requests values from photoQuality table by photoUUID

## 0.0.64
- Clients would like the option to delete from our database as well as delete photo 
entities from s3 buckets. Added an optional field when set to true
will parse the location from photo table and delete the entity from the designated
bucket.
- Clients would like the option to move photos stored in our S3 buckets from one bucket to another.
A rpc was created to allow providing a specified bucket and key with a destination bucket and
optional key for the file to be moved from. 

## 0.0.61
- Add rpc for client facing endpoint ModeratePhotos
- Add rpc for Upserting photo qualities
- Add rpc for Getting photo qualities
- Add rpc for Deleting photo qualities

## 0.0.56
- Provider type is required to limit what providers should reduce photo duplication.

## 0.0.55
- Add auto review menu photo
