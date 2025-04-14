# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: message.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='message.proto',
  package='doordash_kotlin_grpc_service',
  syntax='proto3',
  serialized_options=_b('\n\033com.doordash.rpc.kotlingrpcP\001Z\nkotlingrpc\210\001\001'),
  serialized_pb=_b('\n\rmessage.proto\x12\x1c\x64oordash_kotlin_grpc_service\"\x0e\n\x0c\x45mptyRequest\"\x0f\n\rEmptyResponse\"\'\n\x14\x43reateMessageRequest\x12\x0f\n\x07message\x18\x01 \x01(\t\"\'\n\x13GetMessagesResponse\x12\x10\n\x08messages\x18\x01 \x03(\t2\x8e\x02\n\x11KotlinGRPCService\x12}\n\x1a\x43reateMessageForSQSExample\x12\x32.doordash_kotlin_grpc_service.CreateMessageRequest\x1a+.doordash_kotlin_grpc_service.EmptyResponse\x12z\n\x19GetMessagesFromSQSExample\x12*.doordash_kotlin_grpc_service.EmptyRequest\x1a\x31.doordash_kotlin_grpc_service.GetMessagesResponseB.\n\x1b\x63om.doordash.rpc.kotlingrpcP\x01Z\nkotlingrpc\x88\x01\x01\x62\x06proto3')
)




_EMPTYREQUEST = _descriptor.Descriptor(
  name='EmptyRequest',
  full_name='doordash_kotlin_grpc_service.EmptyRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=47,
  serialized_end=61,
)


_EMPTYRESPONSE = _descriptor.Descriptor(
  name='EmptyResponse',
  full_name='doordash_kotlin_grpc_service.EmptyResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=78,
)


_CREATEMESSAGEREQUEST = _descriptor.Descriptor(
  name='CreateMessageRequest',
  full_name='doordash_kotlin_grpc_service.CreateMessageRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='doordash_kotlin_grpc_service.CreateMessageRequest.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=119,
)


_GETMESSAGESRESPONSE = _descriptor.Descriptor(
  name='GetMessagesResponse',
  full_name='doordash_kotlin_grpc_service.GetMessagesResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='messages', full_name='doordash_kotlin_grpc_service.GetMessagesResponse.messages', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=121,
  serialized_end=160,
)

DESCRIPTOR.message_types_by_name['EmptyRequest'] = _EMPTYREQUEST
DESCRIPTOR.message_types_by_name['EmptyResponse'] = _EMPTYRESPONSE
DESCRIPTOR.message_types_by_name['CreateMessageRequest'] = _CREATEMESSAGEREQUEST
DESCRIPTOR.message_types_by_name['GetMessagesResponse'] = _GETMESSAGESRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EmptyRequest = _reflection.GeneratedProtocolMessageType('EmptyRequest', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYREQUEST,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:doordash_kotlin_grpc_service.EmptyRequest)
  })
_sym_db.RegisterMessage(EmptyRequest)

EmptyResponse = _reflection.GeneratedProtocolMessageType('EmptyResponse', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYRESPONSE,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:doordash_kotlin_grpc_service.EmptyResponse)
  })
_sym_db.RegisterMessage(EmptyResponse)

CreateMessageRequest = _reflection.GeneratedProtocolMessageType('CreateMessageRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEMESSAGEREQUEST,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:doordash_kotlin_grpc_service.CreateMessageRequest)
  })
_sym_db.RegisterMessage(CreateMessageRequest)

GetMessagesResponse = _reflection.GeneratedProtocolMessageType('GetMessagesResponse', (_message.Message,), {
  'DESCRIPTOR' : _GETMESSAGESRESPONSE,
  '__module__' : 'message_pb2'
  # @@protoc_insertion_point(class_scope:doordash_kotlin_grpc_service.GetMessagesResponse)
  })
_sym_db.RegisterMessage(GetMessagesResponse)


DESCRIPTOR._options = None

_KOTLINGRPCSERVICE = _descriptor.ServiceDescriptor(
  name='KotlinGRPCService',
  full_name='doordash_kotlin_grpc_service.KotlinGRPCService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=163,
  serialized_end=433,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateMessageForSQSExample',
    full_name='doordash_kotlin_grpc_service.KotlinGRPCService.CreateMessageForSQSExample',
    index=0,
    containing_service=None,
    input_type=_CREATEMESSAGEREQUEST,
    output_type=_EMPTYRESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetMessagesFromSQSExample',
    full_name='doordash_kotlin_grpc_service.KotlinGRPCService.GetMessagesFromSQSExample',
    index=1,
    containing_service=None,
    input_type=_EMPTYREQUEST,
    output_type=_GETMESSAGESRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_KOTLINGRPCSERVICE)

DESCRIPTOR.services_by_name['KotlinGRPCService'] = _KOTLINGRPCSERVICE

# @@protoc_insertion_point(module_scope)
