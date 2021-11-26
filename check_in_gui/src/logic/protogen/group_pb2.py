# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: group.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='group.proto',
  package='group',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bgroup.proto\x12\x05group\"<\n\x12\x43reateGroupRequest\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x18\n\x10\x63reator_username\x18\x02 \x01(\t\"@\n\x18\x41\x64\x64StudentToGroupRequest\x12\x12\n\nstudent_id\x18\x01 \x01(\x05\x12\x10\n\x08group_id\x18\x02 \x01(\x05\"E\n\x1dRemoveStudentFromGroupRequest\x12\x12\n\nstudent_id\x18\x01 \x01(\x05\x12\x10\n\x08group_id\x18\x02 \x01(\x05\"&\n\x12\x44\x65leteGroupRequest\x12\x10\n\x08group_id\x18\x01 \x01(\x05\"\"\n\x13\x43reateGroupResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\"(\n\x19\x41\x64\x64StudentToGroupResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\"-\n\x1eRemoveStudentFromGroupResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t\"\"\n\x13\x44\x65leteGroupResponse\x12\x0b\n\x03msg\x18\x01 \x01(\t2\xda\x02\n\x05Group\x12\x46\n\x0b\x43reateGroup\x12\x19.group.CreateGroupRequest\x1a\x1a.group.CreateGroupResponse\"\x00\x12X\n\x11\x41\x64\x64StudentToGroup\x12\x1f.group.AddStudentToGroupRequest\x1a .group.AddStudentToGroupResponse\"\x00\x12g\n\x16RemoveStudentFromGroup\x12$.group.RemoveStudentFromGroupRequest\x1a%.group.RemoveStudentFromGroupResponse\"\x00\x12\x46\n\x0b\x44\x65leteGroup\x12\x19.group.DeleteGroupRequest\x1a\x1a.group.DeleteGroupResponse\"\x00\x62\x06proto3'
)




_CREATEGROUPREQUEST = _descriptor.Descriptor(
  name='CreateGroupRequest',
  full_name='group.CreateGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='group.CreateGroupRequest.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='creator_username', full_name='group.CreateGroupRequest.creator_username', index=1,
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
  serialized_start=22,
  serialized_end=82,
)


_ADDSTUDENTTOGROUPREQUEST = _descriptor.Descriptor(
  name='AddStudentToGroupRequest',
  full_name='group.AddStudentToGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='student_id', full_name='group.AddStudentToGroupRequest.student_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='group.AddStudentToGroupRequest.group_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=84,
  serialized_end=148,
)


_REMOVESTUDENTFROMGROUPREQUEST = _descriptor.Descriptor(
  name='RemoveStudentFromGroupRequest',
  full_name='group.RemoveStudentFromGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='student_id', full_name='group.RemoveStudentFromGroupRequest.student_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='group_id', full_name='group.RemoveStudentFromGroupRequest.group_id', index=1,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=150,
  serialized_end=219,
)


_DELETEGROUPREQUEST = _descriptor.Descriptor(
  name='DeleteGroupRequest',
  full_name='group.DeleteGroupRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='group.DeleteGroupRequest.group_id', index=0,
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
  serialized_start=221,
  serialized_end=259,
)


_CREATEGROUPRESPONSE = _descriptor.Descriptor(
  name='CreateGroupResponse',
  full_name='group.CreateGroupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='group.CreateGroupResponse.msg', index=0,
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
  serialized_start=261,
  serialized_end=295,
)


_ADDSTUDENTTOGROUPRESPONSE = _descriptor.Descriptor(
  name='AddStudentToGroupResponse',
  full_name='group.AddStudentToGroupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='group.AddStudentToGroupResponse.msg', index=0,
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
  serialized_start=297,
  serialized_end=337,
)


_REMOVESTUDENTFROMGROUPRESPONSE = _descriptor.Descriptor(
  name='RemoveStudentFromGroupResponse',
  full_name='group.RemoveStudentFromGroupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='group.RemoveStudentFromGroupResponse.msg', index=0,
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
  serialized_start=339,
  serialized_end=384,
)


_DELETEGROUPRESPONSE = _descriptor.Descriptor(
  name='DeleteGroupResponse',
  full_name='group.DeleteGroupResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='group.DeleteGroupResponse.msg', index=0,
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
  serialized_start=386,
  serialized_end=420,
)

DESCRIPTOR.message_types_by_name['CreateGroupRequest'] = _CREATEGROUPREQUEST
DESCRIPTOR.message_types_by_name['AddStudentToGroupRequest'] = _ADDSTUDENTTOGROUPREQUEST
DESCRIPTOR.message_types_by_name['RemoveStudentFromGroupRequest'] = _REMOVESTUDENTFROMGROUPREQUEST
DESCRIPTOR.message_types_by_name['DeleteGroupRequest'] = _DELETEGROUPREQUEST
DESCRIPTOR.message_types_by_name['CreateGroupResponse'] = _CREATEGROUPRESPONSE
DESCRIPTOR.message_types_by_name['AddStudentToGroupResponse'] = _ADDSTUDENTTOGROUPRESPONSE
DESCRIPTOR.message_types_by_name['RemoveStudentFromGroupResponse'] = _REMOVESTUDENTFROMGROUPRESPONSE
DESCRIPTOR.message_types_by_name['DeleteGroupResponse'] = _DELETEGROUPRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

CreateGroupRequest = _reflection.GeneratedProtocolMessageType('CreateGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _CREATEGROUPREQUEST,
  '__module__' : 'group_pb2'
  # @@protoc_insertion_point(class_scope:group.CreateGroupRequest)
  })
_sym_db.RegisterMessage(CreateGroupRequest)

AddStudentToGroupRequest = _reflection.GeneratedProtocolMessageType('AddStudentToGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _ADDSTUDENTTOGROUPREQUEST,
  '__module__' : 'group_pb2'
  # @@protoc_insertion_point(class_scope:group.AddStudentToGroupRequest)
  })
_sym_db.RegisterMessage(AddStudentToGroupRequest)

RemoveStudentFromGroupRequest = _reflection.GeneratedProtocolMessageType('RemoveStudentFromGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _REMOVESTUDENTFROMGROUPREQUEST,
  '__module__' : 'group_pb2'
  # @@protoc_insertion_point(class_scope:group.RemoveStudentFromGroupRequest)
  })
_sym_db.RegisterMessage(RemoveStudentFromGroupRequest)

DeleteGroupRequest = _reflection.GeneratedProtocolMessageType('DeleteGroupRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETEGROUPREQUEST,
  '__module__' : 'group_pb2'
  # @@protoc_insertion_point(class_scope:group.DeleteGroupRequest)
  })
_sym_db.RegisterMessage(DeleteGroupRequest)

CreateGroupResponse = _reflection.GeneratedProtocolMessageType('CreateGroupResponse', (_message.Message,), {
  'DESCRIPTOR' : _CREATEGROUPRESPONSE,
  '__module__' : 'group_pb2'
  # @@protoc_insertion_point(class_scope:group.CreateGroupResponse)
  })
_sym_db.RegisterMessage(CreateGroupResponse)

AddStudentToGroupResponse = _reflection.GeneratedProtocolMessageType('AddStudentToGroupResponse', (_message.Message,), {
  'DESCRIPTOR' : _ADDSTUDENTTOGROUPRESPONSE,
  '__module__' : 'group_pb2'
  # @@protoc_insertion_point(class_scope:group.AddStudentToGroupResponse)
  })
_sym_db.RegisterMessage(AddStudentToGroupResponse)

RemoveStudentFromGroupResponse = _reflection.GeneratedProtocolMessageType('RemoveStudentFromGroupResponse', (_message.Message,), {
  'DESCRIPTOR' : _REMOVESTUDENTFROMGROUPRESPONSE,
  '__module__' : 'group_pb2'
  # @@protoc_insertion_point(class_scope:group.RemoveStudentFromGroupResponse)
  })
_sym_db.RegisterMessage(RemoveStudentFromGroupResponse)

DeleteGroupResponse = _reflection.GeneratedProtocolMessageType('DeleteGroupResponse', (_message.Message,), {
  'DESCRIPTOR' : _DELETEGROUPRESPONSE,
  '__module__' : 'group_pb2'
  # @@protoc_insertion_point(class_scope:group.DeleteGroupResponse)
  })
_sym_db.RegisterMessage(DeleteGroupResponse)



_GROUP = _descriptor.ServiceDescriptor(
  name='Group',
  full_name='group.Group',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=423,
  serialized_end=769,
  methods=[
  _descriptor.MethodDescriptor(
    name='CreateGroup',
    full_name='group.Group.CreateGroup',
    index=0,
    containing_service=None,
    input_type=_CREATEGROUPREQUEST,
    output_type=_CREATEGROUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='AddStudentToGroup',
    full_name='group.Group.AddStudentToGroup',
    index=1,
    containing_service=None,
    input_type=_ADDSTUDENTTOGROUPREQUEST,
    output_type=_ADDSTUDENTTOGROUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='RemoveStudentFromGroup',
    full_name='group.Group.RemoveStudentFromGroup',
    index=2,
    containing_service=None,
    input_type=_REMOVESTUDENTFROMGROUPREQUEST,
    output_type=_REMOVESTUDENTFROMGROUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='DeleteGroup',
    full_name='group.Group.DeleteGroup',
    index=3,
    containing_service=None,
    input_type=_DELETEGROUPREQUEST,
    output_type=_DELETEGROUPRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_GROUP)

DESCRIPTOR.services_by_name['Group'] = _GROUP

# @@protoc_insertion_point(module_scope)
