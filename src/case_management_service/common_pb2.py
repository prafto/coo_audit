# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: case-management-service/common.proto
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
    'case-management-service/common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n$case-management-service/common.proto\x12\x1a\x63\x61se_management_service.v1\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1egoogle/protobuf/wrappers.proto\"8\n\x17OffsetPaginationOptions\x12\x0e\n\x06offset\x18\x01 \x01(\x05\x12\r\n\x05limit\x18\x02 \x01(\x05\"s\n\x11PaginationOptions\x12T\n\x15offset_paging_options\x18\x01 \x01(\x0b\x32\x33.case_management_service.v1.OffsetPaginationOptionsH\x00\x42\x08\n\x06paging\"\xe1\x01\n\x11TimeFilterOptions\x12\x31\n\rcreated_after\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0e\x63reated_before\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x31\n\rupdated_after\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x32\n\x0eupdated_before\x18\x04 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\"|\n\x12\x44\x65liveryIdentifier\x12\x31\n\x0b\x64\x65livery_id\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x33\n\rdelivery_uuid\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\xf1\x04\n\rFilterOptions\x12H\n\x0e\x66ilter_options\x18\x03 \x03(\x0b\x32\x30.case_management_service.v1.FilterOptions.Option\x12=\n\x0crequest_type\x18\x04 \x01(\x0e\x32\'.case_management_service.v1.RequestType\x1a\xbc\x01\n\x06Option\x12\x45\n\tfilter_by\x18\x01 \x01(\x0e\x32\x32.case_management_service.v1.FilterOptions.FilterBy\x12\x32\n\x0c\x66ilter_value\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x37\n\x11\x66ilter_value_list\x18\x03 \x03(\x0b\x32\x1c.google.protobuf.StringValue\"\xf2\x01\n\x08\x46ilterBy\x12\x19\n\x15\x46ILTER_BY_UNSPECIFIED\x10\x00\x12\x16\n\x12\x46ILTER_BY_AGENT_ID\x10\x01\x12\x15\n\x11\x46ILTER_BY_CASE_ID\x10\x02\x12\x1a\n\x16\x46ILTER_BY_CASE_SUBJECT\x10\x03\x12\x19\n\x15\x46ILTER_BY_CASE_STATUS\x10\x04\x12\x18\n\x14\x46ILTER_BY_QUEUE_NAME\x10\x05\x12\x1b\n\x17\x46ILTER_BY_QUEUE_CHANNEL\x10\x06\x12\x1a\n\x16\x46ILTER_BY_AGENT_STATUS\x10\x07\x12\x12\n\x0e\x46ILTER_BY_SITE\x10\x08J\x04\x08\x01\x10\x02J\x04\x08\x02\x10\x03R\tfilter_byR\x0c\x66ilter_value*t\n\x0eTimeFilterType\x12 \n\x1cTIME_FILTER_TYPE_UNSPECIFIED\x10\x00\x12\x1f\n\x1bTIME_FILTER_TYPE_CREATED_AT\x10\x01\x12\x1f\n\x1bTIME_FILTER_TYPE_UPDATED_AT\x10\x02*\x9e\x01\n\x0b\x43hannelType\x12\x1c\n\x18\x43HANNEL_TYPE_UNSPECIFIED\x10\x00\x12\x15\n\x11\x43HANNEL_TYPE_CHAT\x10\x01\x12\x16\n\x12\x43HANNEL_TYPE_PHONE\x10\x02\x12\x16\n\x12\x43HANNEL_TYPE_AGENT\x10\x03\x12\x14\n\x10\x43HANNEL_TYPE_API\x10\x04\x12\x14\n\x10\x43HANNEL_TYPE_WEB\x10\x05*b\n\x0bRequestType\x12\x1c\n\x18REQUEST_TYPE_UNSPECIFIED\x10\x00\x12\x17\n\x13REQUEST_TYPE_AGENTS\x10\x01\x12\x1c\n\x18REQUEST_TYPE_SUPERVISORS\x10\x02\x42&\n\x1f\x63om.doordash.rpc.casemanagementP\x01\x88\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'case_management_service.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\037com.doordash.rpc.casemanagementP\001\210\001\001'
  _globals['_TIMEFILTERTYPE']._serialized_start=1290
  _globals['_TIMEFILTERTYPE']._serialized_end=1406
  _globals['_CHANNELTYPE']._serialized_start=1409
  _globals['_CHANNELTYPE']._serialized_end=1567
  _globals['_REQUESTTYPE']._serialized_start=1569
  _globals['_REQUESTTYPE']._serialized_end=1667
  _globals['_OFFSETPAGINATIONOPTIONS']._serialized_start=133
  _globals['_OFFSETPAGINATIONOPTIONS']._serialized_end=189
  _globals['_PAGINATIONOPTIONS']._serialized_start=191
  _globals['_PAGINATIONOPTIONS']._serialized_end=306
  _globals['_TIMEFILTEROPTIONS']._serialized_start=309
  _globals['_TIMEFILTEROPTIONS']._serialized_end=534
  _globals['_DELIVERYIDENTIFIER']._serialized_start=536
  _globals['_DELIVERYIDENTIFIER']._serialized_end=660
  _globals['_FILTEROPTIONS']._serialized_start=663
  _globals['_FILTEROPTIONS']._serialized_end=1288
  _globals['_FILTEROPTIONS_OPTION']._serialized_start=818
  _globals['_FILTEROPTIONS_OPTION']._serialized_end=1006
  _globals['_FILTEROPTIONS_FILTERBY']._serialized_start=1009
  _globals['_FILTEROPTIONS_FILTERBY']._serialized_end=1251
# @@protoc_insertion_point(module_scope)
