
  
from logic.protogen import group_pb2_grpc
from logic.protogen import group_pb2
from utils.config import CONFIG
import grpc

_CLIENT_CONFIG: str = CONFIG["grpc"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return group_pb2_grpc.GroupStub(channel)


# Returns status code
def create_group(name) -> str:
    return _create_stub().CreateGroup(
        group_pb2.CreateGroupRequest(
            name=name
        )
    )

#  Returns status code
def add_student_to_group(student_id, group_id):
    return _create_stub().AddStudentToGroup(
        group_pb2.AddStudentToGroupRequest(
            student_id=student_id,
            group_id=group_id,
        )
    )

# Returns status code
def remove_student_from_group(student_id, group_id):
    return _create_stub().RemoveStudentFromGroup(
        group_pb2.RemoveStudentFromGroupRequest(
            student_id=student_id,
            group_id=group_id,
        )
    )

# Returns status code
def delete_group(group_id):
    return _create_stub().DeleteGroup(
        group_pb2.DeleteGroupRequest(
            group_id=group_id,
        )
    )
    
    
    




