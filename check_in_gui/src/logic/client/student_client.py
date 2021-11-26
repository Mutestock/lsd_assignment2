from logic.protogen import student_pb2_grpc
from logic.protogen import student_pb2
from utils.config import CONFIG
import grpc

_CLIENT_CONFIG: str = CONFIG["grpc"]

def _create_stub():
    channel = grpc.insecure_channel(
        f"{_CLIENT_CONFIG['host']}:{_CLIENT_CONFIG['port']}"
    )
    return student_pb2_grpc.StudentStub(channel)


# Returns true/false depending on check in success
def code_check_in(code, ip, username) -> bool:
    return _create_stub().CodeCheckIn(
        student_pb2.CodeCheckInRequest(
            code=code,
            ip=ip,
            username=username
        )
    )
    

def get_stats(id):
    return _create_stub().GetStats(
        student_pb2.GetStatsRequest(
            id=id
        )
    )
    

def get_all_students():
    return _create_stub().GetAllStudents(
        student_pb2.GetAllStudentsRequest()
    )
    
    