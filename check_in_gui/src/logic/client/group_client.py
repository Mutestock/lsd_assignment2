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
def create_group(name, creator_username) -> str:
    return _create_stub().CreateGroup(
        group_pb2.CreateGroupRequest(
            name=name,
            creator_username=creator_username,
        )
    )


#  Returns status code
def add_student_to_group(student_name, group_name):
    return _create_stub().AddStudentToGroup(
        group_pb2.AddStudentToGroupRequest(
            student_name=student_name,
            group_name=group_name,
        )
    )


# Returns status code
def remove_student_from_group(student_name, group_name):
    return _create_stub().RemoveStudentFromGroup(
        group_pb2.RemoveStudentFromGroupRequest(
            student_name=student_name,
            group_name=group_name,
        )
    )


# Returns status code
def delete_group(group_name):
    return _create_stub().DeleteGroup(
        group_pb2.DeleteGroupRequest(
            group_name=group_name,
        )
    )


def get_all_groups_by_username(username):
    return _create_stub().GetAllGroupsByUsername(
        group_pb2.GetAllGroupsByUsernameRequest(username=username)
    )


def get_all_students_by_group_name(group_name):
    return _create_stub().GetAllStudentsByGroupName(
        group_pb2.GetAllStudentsByGroupNameRequest(group_name=group_name)
    )
