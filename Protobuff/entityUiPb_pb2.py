# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: entityUiPb.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import timeUiPb_pb2 as timeUiPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='entityUiPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10\x65ntityUiPb.proto\x1a\x0etimeUiPb.proto\"e\n\nEntityUiPb\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0f\n\x07version\x18\x02 \x01(\x05\x12\x1d\n\x08lifeTime\x18\x03 \x01(\x0e\x32\x0b.StatusEnum\x12\x1b\n\x06locale\x18\x04 \x01(\x0b\x32\x0b.LocaleUiPb\"4\n\nLocaleUiPb\x12&\n\x0f\x64\x65\x66\x61ultTimeZone\x18\x01 \x01(\x0e\x32\r.TimeZoneEnum*U\n\nStatusEnum\x12\x12\n\x0eUNKNOWN_STATUS\x10\x00\x12\n\n\x06\x41\x43TIVE\x10\x01\x12\x0b\n\x07\x44\x45LETED\x10\x02\x12\r\n\tSUSPUNDED\x10\x03\x12\x0b\n\x07\x42LOCKED\x10\x04\x62\x06proto3'
  ,
  dependencies=[timeUiPb__pb2.DESCRIPTOR,])

_STATUSENUM = _descriptor.EnumDescriptor(
  name='StatusEnum',
  full_name='StatusEnum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_STATUS', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ACTIVE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DELETED', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUSPUNDED', index=3, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='BLOCKED', index=4, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=193,
  serialized_end=278,
)
_sym_db.RegisterEnumDescriptor(_STATUSENUM)

StatusEnum = enum_type_wrapper.EnumTypeWrapper(_STATUSENUM)
UNKNOWN_STATUS = 0
ACTIVE = 1
DELETED = 2
SUSPUNDED = 3
BLOCKED = 4



_ENTITYUIPB = _descriptor.Descriptor(
  name='EntityUiPb',
  full_name='EntityUiPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='EntityUiPb.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='version', full_name='EntityUiPb.version', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='lifeTime', full_name='EntityUiPb.lifeTime', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='locale', full_name='EntityUiPb.locale', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_end=137,
)


_LOCALEUIPB = _descriptor.Descriptor(
  name='LocaleUiPb',
  full_name='LocaleUiPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='defaultTimeZone', full_name='LocaleUiPb.defaultTimeZone', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=139,
  serialized_end=191,
)

_ENTITYUIPB.fields_by_name['lifeTime'].enum_type = _STATUSENUM
_ENTITYUIPB.fields_by_name['locale'].message_type = _LOCALEUIPB
_LOCALEUIPB.fields_by_name['defaultTimeZone'].enum_type = timeUiPb__pb2._TIMEZONEENUM
DESCRIPTOR.message_types_by_name['EntityUiPb'] = _ENTITYUIPB
DESCRIPTOR.message_types_by_name['LocaleUiPb'] = _LOCALEUIPB
DESCRIPTOR.enum_types_by_name['StatusEnum'] = _STATUSENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EntityUiPb = _reflection.GeneratedProtocolMessageType('EntityUiPb', (_message.Message,), {
  'DESCRIPTOR' : _ENTITYUIPB,
  '__module__' : 'entityUiPb_pb2'
  # @@protoc_insertion_point(class_scope:EntityUiPb)
  })
_sym_db.RegisterMessage(EntityUiPb)

LocaleUiPb = _reflection.GeneratedProtocolMessageType('LocaleUiPb', (_message.Message,), {
  'DESCRIPTOR' : _LOCALEUIPB,
  '__module__' : 'entityUiPb_pb2'
  # @@protoc_insertion_point(class_scope:LocaleUiPb)
  })
_sym_db.RegisterMessage(LocaleUiPb)


# @@protoc_insertion_point(module_scope)
