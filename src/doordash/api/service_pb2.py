# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: doordash.api/service.proto
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
    'doordash.api/service.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from doordash.api import common_pb2 as doordash_dot_api_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x64oordash.api/service.proto\x12\x0c\x64oordash.api\x1a\x19\x64oordash.api/common.proto\"\x86\x02\n\x0bServiceRule\x12\"\n\x05owner\x18\x01 \x01(\x0b\x32\x13.doordash.api.Owner\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x0c\n\x04port\x18\x04 \x01(\x05\x12\x12\n\nname_space\x18\x05 \x01(\t\x12\x13\n\x0bname_spaces\x18\x06 \x03(\t\x12\x35\n\x10vertical_domains\x18\x07 \x03(\x0e\x32\x1b.doordash.api.TargetProduct\x12\x14\n\x0c\x61pi_key_name\x18\x08 \x01(\t\x12\x34\n\x0ftarget_products\x18\t \x03(\x0e\x32\x1b.doordash.api.TargetProductBj\n\x10\x63om.doordash.apiB\x0cServiceProtoP\x01Z<github.com/doordash/services-protobuf/generated/doordash.api\xf8\x01\x01\xa2\x02\x04\x44\x41PIb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'doordash.api.service_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\020com.doordash.apiB\014ServiceProtoP\001Z<github.com/doordash/services-protobuf/generated/doordash.api\370\001\001\242\002\004DAPI'
  _globals['_SERVICERULE']._serialized_start=72
  _globals['_SERVICERULE']._serialized_end=334
# @@protoc_insertion_point(module_scope)
