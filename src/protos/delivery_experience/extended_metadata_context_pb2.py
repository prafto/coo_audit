# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: delivery_experience/extended_metadata_context.proto
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
    'delivery_experience/extended_metadata_context.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from postal_service import messaging_pb2 as postal__service_dot_messaging__pb2
from delivery_experience import order_status_pb2 as delivery__experience_dot_order__status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n3delivery_experience/extended_metadata_context.proto\x12\x16\x64\x65livery_experience.v1\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1epostal_service/messaging.proto\x1a&delivery_experience/order_status.proto\"\xb8\x01\n#PostCheckoutExtendedMetadataContext\x12J\n\x15\x63ountdown_bar_details\x18\x01 \x01(\x0b\x32+.delivery_experience.v1.CountdownBarDetails\x12\x45\n\x12translated_strings\x18\x02 \x01(\x0b\x32).delivery_experience.v1.TranslatedStringsB\x1a\n\x13\x64\x65livery.experienceP\x01\x88\x01\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'delivery_experience.extended_metadata_context_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\023delivery.experienceP\001\210\001\001'
  _globals['_POSTCHECKOUTEXTENDEDMETADATACONTEXT']._serialized_start=184
  _globals['_POSTCHECKOUTEXTENDEDMETADATACONTEXT']._serialized_end=368
# @@protoc_insertion_point(module_scope)
