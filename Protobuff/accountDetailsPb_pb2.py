# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: accountDetailsPb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='accountDetailsPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x16\x61\x63\x63ountDetailsPb.proto\"\x91\x01\n\x10\x41\x63\x63ountDetailsPb\x12\x11\n\taccountNo\x18\x01 \x01(\t\x12\x10\n\x08ifscCode\x18\x02 \x01(\t\x12\x15\n\rrecipientName\x18\x03 \x01(\t\x12\x10\n\x08\x62\x61nkName\x18\x04 \x01(\t\x12\x0e\n\x06\x62ranch\x18\x05 \x01(\t\x12\x1f\n\tgooglePay\x18\x06 \x01(\x0b\x32\x0c.GooglePayPb\"\x1c\n\x0bGooglePayPb\x12\r\n\x05upiId\x18\x01 \x01(\tb\x06proto3'
)




_ACCOUNTDETAILSPB = _descriptor.Descriptor(
  name='AccountDetailsPb',
  full_name='AccountDetailsPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='accountNo', full_name='AccountDetailsPb.accountNo', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ifscCode', full_name='AccountDetailsPb.ifscCode', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='recipientName', full_name='AccountDetailsPb.recipientName', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='bankName', full_name='AccountDetailsPb.bankName', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='branch', full_name='AccountDetailsPb.branch', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='googlePay', full_name='AccountDetailsPb.googlePay', index=5,
      number=6, type=11, cpp_type=10, label=1,
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
  serialized_start=27,
  serialized_end=172,
)


_GOOGLEPAYPB = _descriptor.Descriptor(
  name='GooglePayPb',
  full_name='GooglePayPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='upiId', full_name='GooglePayPb.upiId', index=0,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=174,
  serialized_end=202,
)

_ACCOUNTDETAILSPB.fields_by_name['googlePay'].message_type = _GOOGLEPAYPB
DESCRIPTOR.message_types_by_name['AccountDetailsPb'] = _ACCOUNTDETAILSPB
DESCRIPTOR.message_types_by_name['GooglePayPb'] = _GOOGLEPAYPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AccountDetailsPb = _reflection.GeneratedProtocolMessageType('AccountDetailsPb', (_message.Message,), {
  'DESCRIPTOR' : _ACCOUNTDETAILSPB,
  '__module__' : 'accountDetailsPb_pb2'
  # @@protoc_insertion_point(class_scope:AccountDetailsPb)
  })
_sym_db.RegisterMessage(AccountDetailsPb)

GooglePayPb = _reflection.GeneratedProtocolMessageType('GooglePayPb', (_message.Message,), {
  'DESCRIPTOR' : _GOOGLEPAYPB,
  '__module__' : 'accountDetailsPb_pb2'
  # @@protoc_insertion_point(class_scope:GooglePayPb)
  })
_sym_db.RegisterMessage(GooglePayPb)


# @@protoc_insertion_point(module_scope)
