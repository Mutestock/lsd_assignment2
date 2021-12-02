
  
from logic.protogen import teacher_pb2_grpc
from logic.protogen import teacher_pb2
from utils.config import CONFIG
import grpc

_CLIENT_CONFIG: str = CONFIG["grpc"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return teacher_pb2_grpc.TeacherStub(channel)


# Code gets generated from server
def generate_code_and_start(ip, date_time, group_name) -> str:
    return _create_stub().GenerateCodeAndStart(
        teacher_pb2.GenerateCodeAndStartRequest(
            ip_encrypted=ip,
            date_time=date_time,
            group_name=group_name
        )
    )

# Returns status code
def edit_countdown(code, date_time) -> str:
    return _create_stub().EditCountdown(
        teacher_pb2.EditCountdownRequest(
            code=code,
            date_time=date_time
        )
    )   

# Returns status code
def delete_code(code) -> str:
    return _create_stub().DeleteCode(
        teacher_pb2.DeleteCodeRequest(
            code = code,
        )
    )   
