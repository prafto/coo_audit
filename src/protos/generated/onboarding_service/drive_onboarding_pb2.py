# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: onboarding-service/drive_onboarding.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'onboarding-service/drive_onboarding.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from common import common_pb2 as common_dot_common__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from common import service_client_config_pb2 as common_dot_service__client__config__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)onboarding-service/drive_onboarding.proto\x12\x1e\x64oordash_onboarding_service.v1\x1a\x13\x63ommon/common.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\"common/service_client_config.proto\"\x95\x11\n\x18OnboardDriveNewMxRequest\x12\x33\n\ronboarding_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rstore_address\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12:\n\x14store_address_street\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12store_address_city\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x39\n\x13store_address_state\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x15store_address_country\x18\x06 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11store_address_zip\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nstore_name\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x31\n\x0bstore_email\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12store_phone_number\x18\n \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x38\n\x12salesforce_lead_id\x18\x0b \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0fuser_first_name\x18\x0c \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0euser_last_name\x18\r \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11user_phone_number\x18\x0e \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12-\n\x07user_id\x18\x0f \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x30\n\nuser_email\x18\x10 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12X\n\x0bsignup_type\x18\x11 \x01(\x0e\x32\x43.doordash_onboarding_service.v1.OnboardDriveNewMxRequest.SignupType\x12>\n\x19num_addressable_locations\x18\x12 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12.\n\x08language\x18\x13 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12.\n\x08\x63urrency\x18\x14 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12;\n\x15online_order_provider\x18\x15 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x41\n\x1bonline_order_provider_other\x18\x16 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11\x64\x65livery_provider\x18\x17 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rselected_plan\x18\x1c \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x41\n\x1bonline_order_provider_email\x18\x18 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12@\n\x1aonline_order_provider_name\x18\x19 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12z\n\x1a\x64rive_business_information\x18\x1a \x03(\x0b\x32V.doordash_onboarding_service.v1.OnboardDriveNewMxRequest.DriveBusinessInformationEntry\x12k\n\x12\x61\x63\x63ounting_contact\x18\x1b \x03(\x0b\x32O.doordash_onboarding_service.v1.OnboardDriveNewMxRequest.AccountingContactEntry\x12y\n\x1aonline_order_provider_meta\x18\x1d \x03(\x0b\x32U.doordash_onboarding_service.v1.OnboardDriveNewMxRequest.OnlineOrderProviderMetaEntry\x1a?\n\x1d\x44riveBusinessInformationEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a\x38\n\x16\x41\x63\x63ountingContactEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\x1a>\n\x1cOnlineOrderProviderMetaEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"|\n\nSignupType\x12\x1b\n\x17SIGNUP_TYPE_UNSPECIFIED\x10\x00\x12\x1b\n\x17SIGNUP_TYPE_MARKETPLACE\x10\x01\x12\x1d\n\x19SIGNUP_TYPE_SELF_DELIVERY\x10\x02\x12\x15\n\x11SIGNUP_TYPE_DRIVE\x10\x03\"2\n\x19OnboardDriveNewMxResponse\x12\x15\n\ronboarding_id\x18\x01 \x01(\t2\xad\x01\n\x16\x44riveOnboardingService\x12\x88\x01\n\x11OnboardDriveNewMx\x12\x38.doordash_onboarding_service.v1.OnboardDriveNewMxRequest\x1a\x39.doordash_onboarding_service.v1.OnboardDriveNewMxResponse\x1a\x08\xf2\xed\x1e\x04\"\x02\x18\x04\x42\"\n\x1b\x63om.doordash.rpc.onboardingP\x01\x88\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'onboarding_service.drive_onboarding_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\033com.doordash.rpc.onboardingP\001\210\001\001'
  _globals['_ONBOARDDRIVENEWMXREQUEST_DRIVEBUSINESSINFORMATIONENTRY']._loaded_options = None
  _globals['_ONBOARDDRIVENEWMXREQUEST_DRIVEBUSINESSINFORMATIONENTRY']._serialized_options = b'8\001'
  _globals['_ONBOARDDRIVENEWMXREQUEST_ACCOUNTINGCONTACTENTRY']._loaded_options = None
  _globals['_ONBOARDDRIVENEWMXREQUEST_ACCOUNTINGCONTACTENTRY']._serialized_options = b'8\001'
  _globals['_ONBOARDDRIVENEWMXREQUEST_ONLINEORDERPROVIDERMETAENTRY']._loaded_options = None
  _globals['_ONBOARDDRIVENEWMXREQUEST_ONLINEORDERPROVIDERMETAENTRY']._serialized_options = b'8\001'
  _globals['_DRIVEONBOARDINGSERVICE']._loaded_options = None
  _globals['_DRIVEONBOARDINGSERVICE']._serialized_options = b'\362\355\036\004\"\002\030\004'
  _globals['_ONBOARDDRIVENEWMXREQUEST']._serialized_start=200
  _globals['_ONBOARDDRIVENEWMXREQUEST']._serialized_end=2397
  _globals['_ONBOARDDRIVENEWMXREQUEST_DRIVEBUSINESSINFORMATIONENTRY']._serialized_start=2086
  _globals['_ONBOARDDRIVENEWMXREQUEST_DRIVEBUSINESSINFORMATIONENTRY']._serialized_end=2149
  _globals['_ONBOARDDRIVENEWMXREQUEST_ACCOUNTINGCONTACTENTRY']._serialized_start=2151
  _globals['_ONBOARDDRIVENEWMXREQUEST_ACCOUNTINGCONTACTENTRY']._serialized_end=2207
  _globals['_ONBOARDDRIVENEWMXREQUEST_ONLINEORDERPROVIDERMETAENTRY']._serialized_start=2209
  _globals['_ONBOARDDRIVENEWMXREQUEST_ONLINEORDERPROVIDERMETAENTRY']._serialized_end=2271
  _globals['_ONBOARDDRIVENEWMXREQUEST_SIGNUPTYPE']._serialized_start=2273
  _globals['_ONBOARDDRIVENEWMXREQUEST_SIGNUPTYPE']._serialized_end=2397
  _globals['_ONBOARDDRIVENEWMXRESPONSE']._serialized_start=2399
  _globals['_ONBOARDDRIVENEWMXRESPONSE']._serialized_end=2449
  _globals['_DRIVEONBOARDINGSERVICE']._serialized_start=2452
  _globals['_DRIVEONBOARDINGSERVICE']._serialized_end=2625
# @@protoc_insertion_point(module_scope)
