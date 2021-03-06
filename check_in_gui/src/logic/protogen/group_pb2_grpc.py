# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import logic.protogen.group_pb2 as group__pb2


class GroupStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateGroup = channel.unary_unary(
                '/group.Group/CreateGroup',
                request_serializer=group__pb2.CreateGroupRequest.SerializeToString,
                response_deserializer=group__pb2.CreateGroupResponse.FromString,
                )
        self.AddStudentToGroup = channel.unary_unary(
                '/group.Group/AddStudentToGroup',
                request_serializer=group__pb2.AddStudentToGroupRequest.SerializeToString,
                response_deserializer=group__pb2.AddStudentToGroupResponse.FromString,
                )
        self.RemoveStudentFromGroup = channel.unary_unary(
                '/group.Group/RemoveStudentFromGroup',
                request_serializer=group__pb2.RemoveStudentFromGroupRequest.SerializeToString,
                response_deserializer=group__pb2.RemoveStudentFromGroupResponse.FromString,
                )
        self.DeleteGroup = channel.unary_unary(
                '/group.Group/DeleteGroup',
                request_serializer=group__pb2.DeleteGroupRequest.SerializeToString,
                response_deserializer=group__pb2.DeleteGroupResponse.FromString,
                )
        self.GetAllGroupsByUsername = channel.unary_unary(
                '/group.Group/GetAllGroupsByUsername',
                request_serializer=group__pb2.GetAllGroupsByUsernameRequest.SerializeToString,
                response_deserializer=group__pb2.GetAllGroupsByUsernameResponse.FromString,
                )
        self.GetAllStudentsByGroupName = channel.unary_unary(
                '/group.Group/GetAllStudentsByGroupName',
                request_serializer=group__pb2.GetAllStudentsByGroupNameRequest.SerializeToString,
                response_deserializer=group__pb2.GetAllStudentsByGroupNameResponse.FromString,
                )


class GroupServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddStudentToGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RemoveStudentFromGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteGroup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllGroupsByUsername(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetAllStudentsByGroupName(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GroupServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateGroup,
                    request_deserializer=group__pb2.CreateGroupRequest.FromString,
                    response_serializer=group__pb2.CreateGroupResponse.SerializeToString,
            ),
            'AddStudentToGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.AddStudentToGroup,
                    request_deserializer=group__pb2.AddStudentToGroupRequest.FromString,
                    response_serializer=group__pb2.AddStudentToGroupResponse.SerializeToString,
            ),
            'RemoveStudentFromGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.RemoveStudentFromGroup,
                    request_deserializer=group__pb2.RemoveStudentFromGroupRequest.FromString,
                    response_serializer=group__pb2.RemoveStudentFromGroupResponse.SerializeToString,
            ),
            'DeleteGroup': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteGroup,
                    request_deserializer=group__pb2.DeleteGroupRequest.FromString,
                    response_serializer=group__pb2.DeleteGroupResponse.SerializeToString,
            ),
            'GetAllGroupsByUsername': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllGroupsByUsername,
                    request_deserializer=group__pb2.GetAllGroupsByUsernameRequest.FromString,
                    response_serializer=group__pb2.GetAllGroupsByUsernameResponse.SerializeToString,
            ),
            'GetAllStudentsByGroupName': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllStudentsByGroupName,
                    request_deserializer=group__pb2.GetAllStudentsByGroupNameRequest.FromString,
                    response_serializer=group__pb2.GetAllStudentsByGroupNameResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'group.Group', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Group(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/CreateGroup',
            group__pb2.CreateGroupRequest.SerializeToString,
            group__pb2.CreateGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddStudentToGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/AddStudentToGroup',
            group__pb2.AddStudentToGroupRequest.SerializeToString,
            group__pb2.AddStudentToGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RemoveStudentFromGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/RemoveStudentFromGroup',
            group__pb2.RemoveStudentFromGroupRequest.SerializeToString,
            group__pb2.RemoveStudentFromGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteGroup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/DeleteGroup',
            group__pb2.DeleteGroupRequest.SerializeToString,
            group__pb2.DeleteGroupResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllGroupsByUsername(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/GetAllGroupsByUsername',
            group__pb2.GetAllGroupsByUsernameRequest.SerializeToString,
            group__pb2.GetAllGroupsByUsernameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetAllStudentsByGroupName(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/group.Group/GetAllStudentsByGroupName',
            group__pb2.GetAllStudentsByGroupNameRequest.SerializeToString,
            group__pb2.GetAllStudentsByGroupNameResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
