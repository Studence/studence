# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: summaryUiPb.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='summaryUiPb.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x11summaryUiPb.proto\" \n\x0bSummaryUiPb\x12\x11\n\ttotalHits\x18\x01 \x01(\x05\x62\x06proto3'
)




_SUMMARYUIPB = _descriptor.Descriptor(
  name='SummaryUiPb',
  full_name='SummaryUiPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='totalHits', full_name='SummaryUiPb.totalHits', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=21,
  serialized_end=53,
)

DESCRIPTOR.message_types_by_name['SummaryUiPb'] = _SUMMARYUIPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SummaryUiPb = _reflection.GeneratedProtocolMessageType('SummaryUiPb', (_message.Message,), {
  'DESCRIPTOR' : _SUMMARYUIPB,
  '__module__' : 'summaryUiPb_pb2'
  # @@protoc_insertion_point(class_scope:SummaryUiPb)
  })
_sym_db.RegisterMessage(SummaryUiPb)


# @@protoc_insertion_point(module_scope)
