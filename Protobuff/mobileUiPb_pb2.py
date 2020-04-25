# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: mobileUiPb.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='mobileUiPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x10mobileUiPb.proto\":\n\nMobileUiPb\x12\x1c\n\x04\x63ode\x18\x01 \x01(\x0e\x32\x0e.PhoneCodeEnum\x12\x0e\n\x06number\x18\x02 \x01(\t**\n\rPhoneCodeEnum\x12\x10\n\x0cUNKNOWN_CODE\x10\x00\x12\x07\n\x03ISD\x10\x01\x62\x06proto3'
)

_PHONECODEENUM = _descriptor.EnumDescriptor(
  name='PhoneCodeEnum',
  full_name='PhoneCodeEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNKNOWN_CODE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ISD', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=80,
  serialized_end=122,
)
_sym_db.RegisterEnumDescriptor(_PHONECODEENUM)

PhoneCodeEnum = enum_type_wrapper.EnumTypeWrapper(_PHONECODEENUM)
UNKNOWN_CODE = 0
ISD = 1



_MOBILEUIPB = _descriptor.Descriptor(
  name='MobileUiPb',
  full_name='MobileUiPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='MobileUiPb.code', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='number', full_name='MobileUiPb.number', index=1,
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
  serialized_start=20,
  serialized_end=78,
)

_MOBILEUIPB.fields_by_name['code'].enum_type = _PHONECODEENUM
DESCRIPTOR.message_types_by_name['MobileUiPb'] = _MOBILEUIPB
DESCRIPTOR.enum_types_by_name['PhoneCodeEnum'] = _PHONECODEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MobileUiPb = _reflection.GeneratedProtocolMessageType('MobileUiPb', (_message.Message,), {
  'DESCRIPTOR' : _MOBILEUIPB,
  '__module__' : 'mobileUiPb_pb2'
  # @@protoc_insertion_point(class_scope:MobileUiPb)
  })
_sym_db.RegisterMessage(MobileUiPb)


# @@protoc_insertion_point(module_scope)