# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: schoolUiPb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import entityUiPb_pb2 as entityUiPb__pb2
import nameUiPb_pb2 as nameUiPb__pb2
import addressUiPb_pb2 as addressUiPb__pb2
import timeUiPb_pb2 as timeUiPb__pb2
import mobileUiPb_pb2 as mobileUiPb__pb2
import classTypeUiPb_pb2 as classTypeUiPb__pb2
import sectionUiPb_pb2 as sectionUiPb__pb2
import genericRefUiPb_pb2 as genericRefUiPb__pb2
import accountDetailsUiPb_pb2 as accountDetailsUiPb__pb2
import summaryUiPb_pb2 as summaryUiPb__pb2
import booleanTypeUiPb_pb2 as booleanTypeUiPb__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='schoolUiPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x10schoolUiPb.proto\x1a\x10\x65ntityUiPb.proto\x1a\x0enameUiPb.proto\x1a\x11\x61\x64\x64ressUiPb.proto\x1a\x0etimeUiPb.proto\x1a\x10mobileUiPb.proto\x1a\x13\x63lassTypeUiPb.proto\x1a\x11sectionUiPb.proto\x1a\x14genericRefUiPb.proto\x1a\x18\x61\x63\x63ountDetailsUiPb.proto\x1a\x11summaryUiPb.proto\x1a\x15\x62ooleanTypeUiPb.proto\"\xa7\x03\n\nSchoolUiPb\x12\x1b\n\x06\x64\x62Info\x18\x01 \x01(\x0b\x32\x0b.EntityUiPb\x12\x17\n\x04name\x18\x02 \x01(\x0b\x32\t.NameUiPb\x12\x1d\n\x07\x61\x64\x64ress\x18\x03 \x01(\x0b\x32\x0c.AddressUiPb\x12\x1b\n\x06mobile\x18\x04 \x03(\x0b\x32\x0b.MobileUiPb\x12\x1e\n\x0b\x63reatedTime\x18\x05 \x01(\x0b\x32\t.TimeUiPb\x12%\n\x0corganisation\x18\x06 \x01(\x0b\x32\x0f.GenericRefUiPb\x12\x12\n\nschoolCode\x18\x07 \x01(\t\x12+\n\x0e\x61\x63\x63ountUseType\x18\x08 \x01(\x0e\x32\x13.AccountUseTypeEnum\x12+\n\x0e\x61\x63\x63ountDetails\x18\t \x01(\x0b\x32\x13.AccountDetailsUiPb\x12!\n\tclassType\x18\n \x03(\x0e\x32\x0e.ClassTypeEnum\x12%\n\x0bsectionType\x18\x0b \x03(\x0e\x32\x10.SectionTypeEnum\x12(\n\x0e\x61\x63\x63ountSection\x18\x0c \x01(\x0e\x32\x10.BooleanTypeEnum\"\xa0\x01\n\rSchoolUiPbRef\x12\n\n\x02id\x18\x01 \x01(\t\x12%\n\x0corganisation\x18\x02 \x01(\x0b\x32\x0f.GenericRefUiPb\x12\x12\n\nschoolCode\x18\x03 \x01(\t\x12!\n\tclassType\x18\x04 \x03(\x0e\x32\x0e.ClassTypeEnum\x12%\n\x0bsectionType\x18\x05 \x03(\x0e\x32\x10.SectionTypeEnum\"\x19\n\x17SchoolSearchRequestUiPb\"W\n\x18SchoolSearchResponseUiPb\x12\x1d\n\x07summary\x18\x01 \x01(\x0b\x32\x0c.SummaryUiPb\x12\x1c\n\x07results\x18\x02 \x03(\x0b\x32\x0b.SchoolUiPbb\x06proto3'
  ,
  dependencies=[entityUiPb__pb2.DESCRIPTOR,nameUiPb__pb2.DESCRIPTOR,addressUiPb__pb2.DESCRIPTOR,timeUiPb__pb2.DESCRIPTOR,mobileUiPb__pb2.DESCRIPTOR,classTypeUiPb__pb2.DESCRIPTOR,sectionUiPb__pb2.DESCRIPTOR,genericRefUiPb__pb2.DESCRIPTOR,accountDetailsUiPb__pb2.DESCRIPTOR,summaryUiPb__pb2.DESCRIPTOR,booleanTypeUiPb__pb2.DESCRIPTOR,])




_SCHOOLUIPB = _descriptor.Descriptor(
  name='SchoolUiPb',
  full_name='SchoolUiPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='dbInfo', full_name='SchoolUiPb.dbInfo', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='name', full_name='SchoolUiPb.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='address', full_name='SchoolUiPb.address', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mobile', full_name='SchoolUiPb.mobile', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='createdTime', full_name='SchoolUiPb.createdTime', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organisation', full_name='SchoolUiPb.organisation', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schoolCode', full_name='SchoolUiPb.schoolCode', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accountUseType', full_name='SchoolUiPb.accountUseType', index=7,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accountDetails', full_name='SchoolUiPb.accountDetails', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classType', full_name='SchoolUiPb.classType', index=9,
      number=10, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sectionType', full_name='SchoolUiPb.sectionType', index=10,
      number=11, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='accountSection', full_name='SchoolUiPb.accountSection', index=11,
      number=12, type=14, cpp_type=8, label=1,
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
  serialized_start=238,
  serialized_end=661,
)


_SCHOOLUIPBREF = _descriptor.Descriptor(
  name='SchoolUiPbRef',
  full_name='SchoolUiPbRef',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='SchoolUiPbRef.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='organisation', full_name='SchoolUiPbRef.organisation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='schoolCode', full_name='SchoolUiPbRef.schoolCode', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='classType', full_name='SchoolUiPbRef.classType', index=3,
      number=4, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sectionType', full_name='SchoolUiPbRef.sectionType', index=4,
      number=5, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=664,
  serialized_end=824,
)


_SCHOOLSEARCHREQUESTUIPB = _descriptor.Descriptor(
  name='SchoolSearchRequestUiPb',
  full_name='SchoolSearchRequestUiPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
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
  serialized_start=826,
  serialized_end=851,
)


_SCHOOLSEARCHRESPONSEUIPB = _descriptor.Descriptor(
  name='SchoolSearchResponseUiPb',
  full_name='SchoolSearchResponseUiPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='summary', full_name='SchoolSearchResponseUiPb.summary', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='results', full_name='SchoolSearchResponseUiPb.results', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=853,
  serialized_end=940,
)

_SCHOOLUIPB.fields_by_name['dbInfo'].message_type = entityUiPb__pb2._ENTITYUIPB
_SCHOOLUIPB.fields_by_name['name'].message_type = nameUiPb__pb2._NAMEUIPB
_SCHOOLUIPB.fields_by_name['address'].message_type = addressUiPb__pb2._ADDRESSUIPB
_SCHOOLUIPB.fields_by_name['mobile'].message_type = mobileUiPb__pb2._MOBILEUIPB
_SCHOOLUIPB.fields_by_name['createdTime'].message_type = timeUiPb__pb2._TIMEUIPB
_SCHOOLUIPB.fields_by_name['organisation'].message_type = genericRefUiPb__pb2._GENERICREFUIPB
_SCHOOLUIPB.fields_by_name['accountUseType'].enum_type = accountDetailsUiPb__pb2._ACCOUNTUSETYPEENUM
_SCHOOLUIPB.fields_by_name['accountDetails'].message_type = accountDetailsUiPb__pb2._ACCOUNTDETAILSUIPB
_SCHOOLUIPB.fields_by_name['classType'].enum_type = classTypeUiPb__pb2._CLASSTYPEENUM
_SCHOOLUIPB.fields_by_name['sectionType'].enum_type = sectionUiPb__pb2._SECTIONTYPEENUM
_SCHOOLUIPB.fields_by_name['accountSection'].enum_type = booleanTypeUiPb__pb2._BOOLEANTYPEENUM
_SCHOOLUIPBREF.fields_by_name['organisation'].message_type = genericRefUiPb__pb2._GENERICREFUIPB
_SCHOOLUIPBREF.fields_by_name['classType'].enum_type = classTypeUiPb__pb2._CLASSTYPEENUM
_SCHOOLUIPBREF.fields_by_name['sectionType'].enum_type = sectionUiPb__pb2._SECTIONTYPEENUM
_SCHOOLSEARCHRESPONSEUIPB.fields_by_name['summary'].message_type = summaryUiPb__pb2._SUMMARYUIPB
_SCHOOLSEARCHRESPONSEUIPB.fields_by_name['results'].message_type = _SCHOOLUIPB
DESCRIPTOR.message_types_by_name['SchoolUiPb'] = _SCHOOLUIPB
DESCRIPTOR.message_types_by_name['SchoolUiPbRef'] = _SCHOOLUIPBREF
DESCRIPTOR.message_types_by_name['SchoolSearchRequestUiPb'] = _SCHOOLSEARCHREQUESTUIPB
DESCRIPTOR.message_types_by_name['SchoolSearchResponseUiPb'] = _SCHOOLSEARCHRESPONSEUIPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SchoolUiPb = _reflection.GeneratedProtocolMessageType('SchoolUiPb', (_message.Message,), {
  'DESCRIPTOR' : _SCHOOLUIPB,
  '__module__' : 'schoolUiPb_pb2'
  # @@protoc_insertion_point(class_scope:SchoolUiPb)
  })
_sym_db.RegisterMessage(SchoolUiPb)

SchoolUiPbRef = _reflection.GeneratedProtocolMessageType('SchoolUiPbRef', (_message.Message,), {
  'DESCRIPTOR' : _SCHOOLUIPBREF,
  '__module__' : 'schoolUiPb_pb2'
  # @@protoc_insertion_point(class_scope:SchoolUiPbRef)
  })
_sym_db.RegisterMessage(SchoolUiPbRef)

SchoolSearchRequestUiPb = _reflection.GeneratedProtocolMessageType('SchoolSearchRequestUiPb', (_message.Message,), {
  'DESCRIPTOR' : _SCHOOLSEARCHREQUESTUIPB,
  '__module__' : 'schoolUiPb_pb2'
  # @@protoc_insertion_point(class_scope:SchoolSearchRequestUiPb)
  })
_sym_db.RegisterMessage(SchoolSearchRequestUiPb)

SchoolSearchResponseUiPb = _reflection.GeneratedProtocolMessageType('SchoolSearchResponseUiPb', (_message.Message,), {
  'DESCRIPTOR' : _SCHOOLSEARCHRESPONSEUIPB,
  '__module__' : 'schoolUiPb_pb2'
  # @@protoc_insertion_point(class_scope:SchoolSearchResponseUiPb)
  })
_sym_db.RegisterMessage(SchoolSearchResponseUiPb)


# @@protoc_insertion_point(module_scope)
