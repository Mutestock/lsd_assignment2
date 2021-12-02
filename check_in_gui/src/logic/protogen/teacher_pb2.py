# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: teacher.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='teacher.proto',
  package='teacher',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rteacher.proto\x12\x07teacher\"Z\n\x1bGenerateCodeAndStartRequest\x12\x14\n\x0cip_encrypted\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\x12\x12\n\ngroup_name\x18\x03 \x01(\t\"7\n\x14\x45\x64itCountdownRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\x11\n\tdate_time\x18\x02 \x01(\t\"!\n\x11\x44\x65leteCodeRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\",\n\x1cGenerateCodeAndStartResponse\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\"$\n\x15\x45\x64itCountdownResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\"!\n\x12\x44\x65leteCodeResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t2\x8b\x02\n\x07Teacher\x12\x65\n\x14GenerateCodeAndStart\x12$.teacher.GenerateCodeAndStartRequest\x1a%.teacher.GenerateCodeAndStartResponse\"\x00\x12P\n\rEditCountdown\x12\x1d.teacher.EditCountdownRequest\x1a\x1e.teacher.EditCountdownResponse\"\x00\x12G\n\nDeleteCode\x12\x1a.teacher.DeleteCodeRequest\x1a\x1b.teacher.DeleteCodeResponse\"\x00\x62\x06proto3'
)




_GENERATECODEANDSTARTREQUEST = _descriptor.Descriptor(
  name='GenerateCodeAndStartRequest',
  full_name='teacher.GenerateCodeAndStartRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='ip_encrypted', full_name='teacher.GenerateCodeAndStartRequest.ip_encrypted', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_time', full_name='teacher.GenerateCodeAndStartRequest.date_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_name', full_name='teacher.GenerateCodeAndStartRequest.group_name', index=2,
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
  serialized_start=26,
  serialized_end=116,
)


_EDITCOUNTDOWNREQUEST = _descriptor.Descriptor(
  name='EditCountdownRequest',
  full_name='teacher.EditCountdownRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='teacher.EditCountdownRequest.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='date_time', full_name='teacher.EditCountdownRequest.date_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=118,
  serialized_end=173,
)


_DELETECODEREQUEST = _descriptor.Descriptor(
  name='DeleteCodeRequest',
  full_name='teacher.DeleteCodeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='teacher.DeleteCodeRequest.code', index=0,
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
  serialized_start=175,
  serialized_end=208,
)


_GENERATECODEANDSTARTRESPONSE = _descriptor.Descriptor(
  name='GenerateCodeAndStartResponse',
  full_name='teacher.GenerateCodeAndStartResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='teacher.GenerateCodeAndStartResponse.code', index=0,
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
  serialized_start=210,
  serialized_end=254,
)


_EDITCOUNTDOWNRESPONSE = _descriptor.Descriptor(
  name='EditCountdownResponse',
  full_name='teacher.EditCountdownResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='teacher.EditCountdownResponse.msg', index=0,
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
  serialized_start=256,
  serialized_end=292,
)


_DELETECODERESPONSE = _descriptor.Descriptor(
  name='DeleteCodeResponse',
  full_name='teacher.DeleteCodeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='teacher.DeleteCodeResponse.msg', index=0,
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
  serialized_start=294,
  serialized_end=327,
)

DESCRIPTOR.message_types_by_name['GenerateCodeAndStartRequest'] = _GENERATECODEANDSTARTREQUEST
DESCRIPTOR.message_types_by_name['EditCountdownRequest'] = _EDITCOUNTDOWNREQUEST
DESCRIPTOR.message_types_by_name['DeleteCodeRequest'] = _DELETECODEREQUEST
DESCRIPTOR.message_types_by_name['GenerateCodeAndStartResponse'] = _GENERATECODEANDSTARTRESPONSE
DESCRIPTOR.message_types_by_name['EditCountdownResponse'] = _EDITCOUNTDOWNRESPONSE
DESCRIPTOR.message_types_by_name['DeleteCodeResponse'] = _DELETECODERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GenerateCodeAndStartRequest = _reflection.GeneratedProtocolMessageType('GenerateCodeAndStartRequest', (_message.Message,), {
  'DESCRIPTOR' : _GENERATECODEANDSTARTREQUEST,
  '__module__' : 'teacher_pb2'
  # @@protoc_insertion_point(class_scope:teacher.GenerateCodeAndStartRequest)
  })
_sym_db.RegisterMessage(GenerateCodeAndStartRequest)

EditCountdownRequest = _reflection.GeneratedProtocolMessageType('EditCountdownRequest', (_message.Message,), {
  'DESCRIPTOR' : _EDITCOUNTDOWNREQUEST,
  '__module__' : 'teacher_pb2'
  # @@protoc_insertion_point(class_scope:teacher.EditCountdownRequest)
  })
_sym_db.RegisterMessage(EditCountdownRequest)

DeleteCodeRequest = _reflection.GeneratedProtocolMessageType('DeleteCodeRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETECODEREQUEST,
  '__module__' : 'teacher_pb2'
  # @@protoc_insertion_point(class_scope:teacher.DeleteCodeRequest)
  })
_sym_db.RegisterMessage(DeleteCodeRequest)

GenerateCodeAndStartResponse = _reflection.GeneratedProtocolMessageType('GenerateCodeAndStartResponse', (_message.Message,), {
  'DESCRIPTOR' : _GENERATECODEANDSTARTRESPONSE,
  '__module__' : 'teacher_pb2'
  # @@protoc_insertion_point(class_scope:teacher.GenerateCodeAndStartResponse)
  })
_sym_db.RegisterMessage(GenerateCodeAndStartResponse)

EditCountdownResponse = _reflection.GeneratedProtocolMessageType('EditCountdownResponse', (_message.Message,), {
  'DESCRIPTOR' : _EDITCOUNTDOWNRESPONSE,
  '__module__' : 'teacher_pb2'
  # @@protoc_insertion_point(class_scope:teacher.EditCountdownResponse)
  })
_sym_db.RegisterMessage(EditCountdownResponse)

DeleteCodeResponse = _reflection.GeneratedProtocolMessageType('DeleteCodeResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETECODERESPONSE,
  '__module__' : 'teacher_pb2'
  # @@protoc_insertion_point(class_scope:teacher.DeleteCodeResponse)
  })
_sym_db.RegisterMessage(DeleteCodeResponse)



_TEACHER = _descriptor.ServiceDescriptor(
  name='Teacher',
  full_name='teacher.Teacher',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=330,
  serialized_end=597,
  methods=[
  _descriptor.MethodDescriptor(
    name='GenerateCodeAndStart',
    full_name='teacher.Teacher.GenerateCodeAndStart',
    index=0,
    containing_service=None,
    input_type=_GENERATECODEANDSTARTREQUEST,
    output_type=_GENERATECODEANDSTARTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='EditCountdown',
    full_name='teacher.Teacher.EditCountdown',
    index=1,
    containing_service=None,
    input_type=_EDITCOUNTDOWNREQUEST,
    output_type=_EDITCOUNTDOWNRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteCode',
    full_name='teacher.Teacher.DeleteCode',
    index=2,
    containing_service=None,
    input_type=_DELETECODEREQUEST,
    output_type=_DELETECODERESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEACHER)

DESCRIPTOR.services_by_name['Teacher'] = _TEACHER

# @@protoc_insertion_point(module_scope)
