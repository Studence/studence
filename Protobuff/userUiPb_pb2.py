# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: userUiPb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import entityUiPb_pb2 as entityUiPb__pb2
import nameUiPb_pb2 as nameUiPb__pb2
import mobileUiPb_pb2 as mobileUiPb__pb2
import emailUiPb_pb2 as emailUiPb__pb2
import schoolUiPb_pb2 as schoolUiPb__pb2
import timeUiPb_pb2 as timeUiPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='userUiPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0euserUiPb.proto\x1a\x10\x65ntityUiPb.proto\x1a\x0enameUiPb.proto\x1a\x10mobileUiPb.proto\x1a\x0f\x65mailUiPb.proto\x1a\x10schoolUiPb.proto\x1a\x0etimeUiPb.proto\"\xd0\x01\n\x08UserUiPb\x12\x1b\n\x06\x64\x62Info\x18\x01 \x01(\x0b\x32\x0b.EntityUiPb\x12\x17\n\x04name\x18\x02 \x01(\x0b\x32\t.NameUiPb\x12\x1b\n\x06mobile\x18\x03 \x01(\x0b\x32\x0b.MobileUiPb\x12\x19\n\x05\x65mail\x18\x04 \x01(\x0b\x32\n.EmailUiPb\x12!\n\tschoolRef\x18\x05 \x01(\x0b\x32\x0e.SchoolUiPbRef\x12\x13\n\x0bteacherCode\x18\x06 \x01(\t\x12\x1e\n\x0b\x63reatedTime\x18\x07 \x01(\x0b\x32\t.TimeUiPb\"G\n\x0bUserUiPbRef\x12\n\n\x02id\x18\x01 \x01(\t\x12\x17\n\x04name\x18\x02 \x01(\x0b\x32\t.NameUiPb\x12\x13\n\x0bteacherCode\x18\x03 \x01(\tb\x06proto3'
  ,
  dependencies=[entityUiPb__pb2.DESCRIPTOR,nameUiPb__pb2.DESCRIPTOR,mobileUiPb__pb2.DESCRIPTOR,emailUiPb__pb2.DESCRIPTOR,schoolUiPb__pb2.DESCRIPTOR,timeUiPb__pb2.DESCRIPTOR,])




_USERUIPB = _descriptor.Descriptor(
  name='UserUiPb',
  full_name='UserUiPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInfo', full_name='UserUiPb.dbInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='UserUiPb.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mobile', full_name='UserUiPb.mobile', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='email', full_name='UserUiPb.email', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schoolRef', full_name='UserUiPb.schoolRef', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='teacherCode', full_name='UserUiPb.teacherCode', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='createdTime', full_name='UserUiPb.createdTime', index=6,
      number=7, type=11, cpp_type=10, label=1,
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
  serialized_start=122,
  serialized_end=330,
)


_USERUIPBREF = _descriptor.Descriptor(
  name='UserUiPbRef',
  full_name='UserUiPbRef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='UserUiPbRef.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='UserUiPbRef.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='teacherCode', full_name='UserUiPbRef.teacherCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
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
  serialized_start=332,
  serialized_end=403,
)

_USERUIPB.fields_by_name['dbInfo'].message_type = entityUiPb__pb2._ENTITYUIPB
_USERUIPB.fields_by_name['name'].message_type = nameUiPb__pb2._NAMEUIPB
_USERUIPB.fields_by_name['mobile'].message_type = mobileUiPb__pb2._MOBILEUIPB
_USERUIPB.fields_by_name['email'].message_type = emailUiPb__pb2._EMAILUIPB
_USERUIPB.fields_by_name['schoolRef'].message_type = schoolUiPb__pb2._SCHOOLUIPBREF
_USERUIPB.fields_by_name['createdTime'].message_type = timeUiPb__pb2._TIMEUIPB
_USERUIPBREF.fields_by_name['name'].message_type = nameUiPb__pb2._NAMEUIPB
DESCRIPTOR.message_types_by_name['UserUiPb'] = _USERUIPB
DESCRIPTOR.message_types_by_name['UserUiPbRef'] = _USERUIPBREF
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserUiPb = _reflection.GeneratedProtocolMessageType('UserUiPb', (_message.Message,), {
  'DESCRIPTOR' : _USERUIPB,
  '__module__' : 'userUiPb_pb2'
  # @@protoc_insertion_point(class_scope:UserUiPb)
  })
_sym_db.RegisterMessage(UserUiPb)

UserUiPbRef = _reflection.GeneratedProtocolMessageType('UserUiPbRef', (_message.Message,), {
  'DESCRIPTOR' : _USERUIPBREF,
  '__module__' : 'userUiPb_pb2'
  # @@protoc_insertion_point(class_scope:UserUiPbRef)
  })
_sym_db.RegisterMessage(UserUiPbRef)


# @@protoc_insertion_point(module_scope)