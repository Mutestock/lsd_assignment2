
  
from logic.protogen import teacher_pb2_grpc
from logic.protogen import teacher_pb2
from utils.config import CONFIG
import grpc

_CLIENT_CONFIG: str = CONFIG["clients"]["grpc"]["mini-proj"]


def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return teacher_pb2_grpc.TeacherStub(channel)


# Code gets generated from server
def generate_code(ip) -> str:
    return _create_stub.GenerateCode(
        teacher_pb2.GenerateCodeRequest(
            ip=ip
        )
    )

# Returns status code
def start_countdown(millis) -> str:
    return _create_stub.StartCountdown(
        teacher_pb2.StartCountdownRequest(
            millis = millis,
        )
    )   

# In case the teacher needs to extend the time for the students
# Returns status code
def extend_countdown(millis) -> str:
    return _create_stub.ExtendCountdown(
        teacher_pb2.ExtendCountdownRequest(
            millis = millis,
        )
    )   