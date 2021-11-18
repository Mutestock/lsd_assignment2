# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: student.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='student.proto',
  package='student',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rstudent.proto\x12\x07student\"B\n\x12\x43odeCheckInRequest\x12\x0c\n\x04\x63ode\x18\x01 \x01(\t\x12\n\n\x02ip\x18\x02 \x01(\t\x12\x12\n\nstudent_id\x18\x03 \x01(\x05\"\x1d\n\x0fGetStatsRequest\x12\n\n\x02id\x18\x01 \x01(\x05\"\x17\n\x15GetAllStudentsRequest\")\n\x13\x43odeCheckInResponse\x12\x12\n\nchecked_in\x18\x01 \x01(\x08\"\xc1\x01\n\x10GetStatsResponse\x12\x32\n\tall_stats\x18\x01 \x03(\x0b\x32\x1f.student.GetStatsResponse.Stats\x1ay\n\x05Stats\x12\x1a\n\x12\x63hecked_in_on_time\x18\x01 \x01(\x08\x12\x17\n\x0fstart_date_time\x18\x02 \x01(\t\x12\x15\n\rend_date_time\x18\x03 \x01(\t\x12\x10\n\x08username\x18\x04 \x01(\t\x12\x12\n\nis_teacher\x18\x05 \x01(\x08\"\xa7\x01\n\x16GetAllStudentsResponse\x12\x33\n\x05studs\x18\x01 \x03(\x0b\x32$.student.GetAllStudentsResponse.Stud\x1aX\n\x04Stud\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x12\n\nis_teacher\x18\x02 \x01(\x08\x12\x10\n\x08username\x18\x03 \x01(\t\x12\x10\n\x08password\x18\x04 \x01(\t\x12\x0c\n\x04salt\x18\x05 \x01(\t2\xed\x01\n\x07Student\x12J\n\x0b\x43odeCheckIn\x12\x1b.student.CodeCheckInRequest\x1a\x1c.student.CodeCheckInResponse\"\x00\x12\x41\n\x08GetStats\x12\x18.student.GetStatsRequest\x1a\x19.student.GetStatsResponse\"\x00\x12S\n\x0eGetAllStudents\x12\x1e.student.GetAllStudentsRequest\x1a\x1f.student.GetAllStudentsResponse\"\x00\x62\x06proto3'
)




_CODECHECKINREQUEST = _descriptor.Descriptor(
  name='CodeCheckInRequest',
  full_name='student.CodeCheckInRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='code', full_name='student.CodeCheckInRequest.code', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='ip', full_name='student.CodeCheckInRequest.ip', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='student_id', full_name='student.CodeCheckInRequest.student_id', index=2,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=26,
  serialized_end=92,
)


_GETSTATSREQUEST = _descriptor.Descriptor(
  name='GetStatsRequest',
  full_name='student.GetStatsRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='student.GetStatsRequest.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=94,
  serialized_end=123,
)


_GETALLSTUDENTSREQUEST = _descriptor.Descriptor(
  name='GetAllStudentsRequest',
  full_name='student.GetAllStudentsRequest',
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
  serialized_start=125,
  serialized_end=148,
)


_CODECHECKINRESPONSE = _descriptor.Descriptor(
  name='CodeCheckInResponse',
  full_name='student.CodeCheckInResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='checked_in', full_name='student.CodeCheckInResponse.checked_in', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=150,
  serialized_end=191,
)


_GETSTATSRESPONSE_STATS = _descriptor.Descriptor(
  name='Stats',
  full_name='student.GetStatsResponse.Stats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='checked_in_on_time', full_name='student.GetStatsResponse.Stats.checked_in_on_time', index=0,
      number=1, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='start_date_time', full_name='student.GetStatsResponse.Stats.start_date_time', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='end_date_time', full_name='student.GetStatsResponse.Stats.end_date_time', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='student.GetStatsResponse.Stats.username', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_teacher', full_name='student.GetStatsResponse.Stats.is_teacher', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
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
  serialized_start=266,
  serialized_end=387,
)

_GETSTATSRESPONSE = _descriptor.Descriptor(
  name='GetStatsResponse',
  full_name='student.GetStatsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='all_stats', full_name='student.GetStatsResponse.all_stats', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETSTATSRESPONSE_STATS, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=194,
  serialized_end=387,
)


_GETALLSTUDENTSRESPONSE_STUD = _descriptor.Descriptor(
  name='Stud',
  full_name='student.GetAllStudentsResponse.Stud',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='student.GetAllStudentsResponse.Stud.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='is_teacher', full_name='student.GetAllStudentsResponse.Stud.is_teacher', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='username', full_name='student.GetAllStudentsResponse.Stud.username', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='password', full_name='student.GetAllStudentsResponse.Stud.password', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='salt', full_name='student.GetAllStudentsResponse.Stud.salt', index=4,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=469,
  serialized_end=557,
)

_GETALLSTUDENTSRESPONSE = _descriptor.Descriptor(
  name='GetAllStudentsResponse',
  full_name='student.GetAllStudentsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='studs', full_name='student.GetAllStudentsResponse.studs', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[_GETALLSTUDENTSRESPONSE_STUD, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=390,
  serialized_end=557,
)

_GETSTATSRESPONSE_STATS.containing_type = _GETSTATSRESPONSE
_GETSTATSRESPONSE.fields_by_name['all_stats'].message_type = _GETSTATSRESPONSE_STATS
_GETALLSTUDENTSRESPONSE_STUD.containing_type = _GETALLSTUDENTSRESPONSE
_GETALLSTUDENTSRESPONSE.fields_by_name['studs'].message_type = _GETALLSTUDENTSRESPONSE_STUD
DESCRIPTOR.message_types_by_name['CodeCheckInRequest'] = _CODECHECKINREQUEST
DESCRIPTOR.message_types_by_name['GetStatsRequest'] = _GETSTATSREQUEST
DESCRIPTOR.message_types_by_name['GetAllStudentsRequest'] = _GETALLSTUDENTSREQUEST
DESCRIPTOR.message_types_by_name['CodeCheckInResponse'] = _CODECHECKINRESPONSE
DESCRIPTOR.message_types_by_name['GetStatsResponse'] = _GETSTATSRESPONSE
DESCRIPTOR.message_types_by_name['GetAllStudentsResponse'] = _GETALLSTUDENTSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CodeCheckInRequest = _reflection.GeneratedProtocolMessageType('CodeCheckInRequest', (_message.Message,), {
  'DESCRIPTOR' : _CODECHECKINREQUEST,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:student.CodeCheckInRequest)
  })
_sym_db.RegisterMessage(CodeCheckInRequest)

GetStatsRequest = _reflection.GeneratedProtocolMessageType('GetStatsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETSTATSREQUEST,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:student.GetStatsRequest)
  })
_sym_db.RegisterMessage(GetStatsRequest)

GetAllStudentsRequest = _reflection.GeneratedProtocolMessageType('GetAllStudentsRequest', (_message.Message,), {
  'DESCRIPTOR' : _GETALLSTUDENTSREQUEST,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:student.GetAllStudentsRequest)
  })
_sym_db.RegisterMessage(GetAllStudentsRequest)

CodeCheckInResponse = _reflection.GeneratedProtocolMessageType('CodeCheckInResponse', (_message.Message,), {
  'DESCRIPTOR' : _CODECHECKINRESPONSE,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:student.CodeCheckInResponse)
  })
_sym_db.RegisterMessage(CodeCheckInResponse)

GetStatsResponse = _reflection.GeneratedProtocolMessageType('GetStatsResponse', (_message.Message,), {

  'Stats' : _reflection.GeneratedProtocolMessageType('Stats', (_message.Message,), {
    'DESCRIPTOR' : _GETSTATSRESPONSE_STATS,
    '__module__' : 'student_pb2'
    # @@protoc_insertion_point(class_scope:student.GetStatsResponse.Stats)
    })
  ,
  'DESCRIPTOR' : _GETSTATSRESPONSE,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:student.GetStatsResponse)
  })
_sym_db.RegisterMessage(GetStatsResponse)
_sym_db.RegisterMessage(GetStatsResponse.Stats)

GetAllStudentsResponse = _reflection.GeneratedProtocolMessageType('GetAllStudentsResponse', (_message.Message,), {

  'Stud' : _reflection.GeneratedProtocolMessageType('Stud', (_message.Message,), {
    'DESCRIPTOR' : _GETALLSTUDENTSRESPONSE_STUD,
    '__module__' : 'student_pb2'
    # @@protoc_insertion_point(class_scope:student.GetAllStudentsResponse.Stud)
    })
  ,
  'DESCRIPTOR' : _GETALLSTUDENTSRESPONSE,
  '__module__' : 'student_pb2'
  # @@protoc_insertion_point(class_scope:student.GetAllStudentsResponse)
  })
_sym_db.RegisterMessage(GetAllStudentsResponse)
_sym_db.RegisterMessage(GetAllStudentsResponse.Stud)



_STUDENT = _descriptor.ServiceDescriptor(
  name='Student',
  full_name='student.Student',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=560,
  serialized_end=797,
  methods=[
  _descriptor.MethodDescriptor(
    name='CodeCheckIn',
    full_name='student.Student.CodeCheckIn',
    index=0,
    containing_service=None,
    input_type=_CODECHECKINREQUEST,
    output_type=_CODECHECKINRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetStats',
    full_name='student.Student.GetStats',
    index=1,
    containing_service=None,
    input_type=_GETSTATSREQUEST,
    output_type=_GETSTATSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='GetAllStudents',
    full_name='student.Student.GetAllStudents',
    index=2,
    containing_service=None,
    input_type=_GETALLSTUDENTSREQUEST,
    output_type=_GETALLSTUDENTSRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_STUDENT)

DESCRIPTOR.services_by_name['Student'] = _STUDENT

# @@protoc_insertion_point(module_scope)
