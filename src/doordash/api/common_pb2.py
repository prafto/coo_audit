# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doordash.api/common.proto
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
    'doordash.api/common.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x64oordash.api/common.proto\x12\x0c\x64oordash.api\"M\n\x05Owner\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\t\x12\x15\n\rslack_channel\x18\x03 \x01(\t\x12\x13\n\x0b\x65mail_alias\x18\x04 \x01(\t*\xaf\x01\n\rTargetProduct\x12\x06\n\x02\x43X\x10\x00\x12\x06\n\x02\x44X\x10\x01\x12\x06\n\x02MX\x10\x02\x12\x0c\n\x08INTERNAL\x10\x03\x12\x06\n\x02\x41X\x10\x04\x12\x08\n\x04LCSP\x10\x05\x12\r\n\tMX_PORTAL\x10\x06\x12\r\n\tAX_PORTAL\x10\x07\x12\x10\n\x0c\x41\x44MIN_PORTAL\x10\x08\x12\x17\n\x13\x41UTONOMOUS_DELIVERY\x10\t\x12\x07\n\x03IVR\x10\n\x12\x14\n\x10PHONE_MODERATION\x10\x0b\x42i\n\x10\x63om.doordash.apiB\x0b\x43ommonProtoP\x01Z<github.com/doordash/services-protobuf/generated/doordash.api\xf8\x01\x01\xa2\x02\x04\x44\x41PIb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doordash.api.common_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.doordash.apiB\013CommonProtoP\001Z<github.com/doordash/services-protobuf/generated/doordash.api\370\001\001\242\002\004DAPI'
  _globals['_TARGETPRODUCT']._serialized_start=123
  _globals['_TARGETPRODUCT']._serialized_end=298
  _globals['_OWNER']._serialized_start=43
  _globals['_OWNER']._serialized_end=120
# @@protoc_insertion_point(module_scope)
