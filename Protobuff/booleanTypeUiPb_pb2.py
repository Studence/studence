# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: booleanTypeUiPb.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='booleanTypeUiPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x15\x62ooleanTypeUiPb.proto*3\n\x0f\x42ooleanTypeEnum\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x08\n\x04TRUE\x10\x01\x12\t\n\x05\x46\x41LSE\x10\x02\x62\x06proto3'
)

_BOOLEANTYPEENUM = _descriptor.EnumDescriptor(
  name='BooleanTypeEnum',
  full_name='BooleanTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='TRUE', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='FALSE', index=2, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=25,
  serialized_end=76,
)
_sym_db.RegisterEnumDescriptor(_BOOLEANTYPEENUM)

BooleanTypeEnum = enum_type_wrapper.EnumTypeWrapper(_BOOLEANTYPEENUM)
DEFAULT = 0
TRUE = 1
FALSE = 2


DESCRIPTOR.enum_types_by_name['BooleanTypeEnum'] = _BOOLEANTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
