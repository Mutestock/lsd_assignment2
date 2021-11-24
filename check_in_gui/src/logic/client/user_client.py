from logic.protogen import user_pb2_grpc
from logic.protogen import user_pb2
from utils.config import CONFIG
from models.user import User

import grpc

_CLIENT_CONFIG: str = CONFIG["grpc"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return user_pb2_grpc.UserStub(channel)


# Returns false/true depending on login success
def login(username, password) -> bool:
    return _create_stub().Login(
        user_pb2.LoginRequest(
            username=username,
            password=password,
        )
    )

# Returns a status code
def create_user(user: User) -> str:
    return _create_stub().CreateUser(
        user_pb2.CreateUserRequest(
            username=user.username,
            password=user.password,
            is_teacher=user.is_teacher,
        )
    )
