# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: timePb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import timeUiPb_pb2 as timeUiPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='timePb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x0ctimePb.proto\x1a\x0etimeUiPb.proto\"\x81\x01\n\x06TimePb\x12\x0c\n\x04\x64\x61te\x18\x01 \x01(\t\x12\r\n\x05month\x18\x02 \x01(\t\x12\x0c\n\x04year\x18\x03 \x01(\t\x12\x14\n\x0cmilliseconds\x18\x04 \x01(\x03\x12\x15\n\rformattedDate\x18\x05 \x01(\t\x12\x1f\n\x08timezone\x18\x06 \x01(\x0e\x32\r.TimeZoneEnumb\x06proto3'
  ,
  dependencies=[timeUiPb__pb2.DESCRIPTOR,])




_TIMEPB = _descriptor.Descriptor(
  name='TimePb',
  full_name='TimePb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date', full_name='TimePb.date', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='month', full_name='TimePb.month', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='year', full_name='TimePb.year', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='milliseconds', full_name='TimePb.milliseconds', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='formattedDate', full_name='TimePb.formattedDate', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='timezone', full_name='TimePb.timezone', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=33,
  serialized_end=162,
)

_TIMEPB.fields_by_name['timezone'].enum_type = timeUiPb__pb2._TIMEZONEENUM
DESCRIPTOR.message_types_by_name['TimePb'] = _TIMEPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TimePb = _reflection.GeneratedProtocolMessageType('TimePb', (_message.Message,), {
  'DESCRIPTOR' : _TIMEPB,
  '__module__' : 'timePb_pb2'
  # @@protoc_insertion_point(class_scope:TimePb)
  })
_sym_db.RegisterMessage(TimePb)


# @@protoc_insertion_point(module_scope)
