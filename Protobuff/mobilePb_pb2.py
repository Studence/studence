# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mobilePb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import mobileUiPb_pb2 as mobileUiPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='mobilePb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0emobilePb.proto\x1a\x10mobileUiPb.proto\"8\n\x08MobilePb\x12\x1c\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x0e.PhoneCodeEnum\x12\x0e\n\x06number\x18\x02 \x01(\tb\x06proto3'
  ,
  dependencies=[mobileUiPb__pb2.DESCRIPTOR,])




_MOBILEPB = _descriptor.Descriptor(
  name='MobilePb',
  full_name='MobilePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='MobilePb.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='MobilePb.number', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=36,
  serialized_end=92,
)

_MOBILEPB.fields_by_name['code'].enum_type = mobileUiPb__pb2._PHONECODEENUM
DESCRIPTOR.message_types_by_name['MobilePb'] = _MOBILEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MobilePb = _reflection.GeneratedProtocolMessageType('MobilePb', (_message.Message,), {
  'DESCRIPTOR' : _MOBILEPB,
  '__module__' : 'mobilePb_pb2'
  # @@protoc_insertion_point(class_scope:MobilePb)
  })
_sym_db.RegisterMessage(MobilePb)


# @@protoc_insertion_point(module_scope)
