# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import bridge_pb2 as api_dot_v1_dot_ovm_dot_bridge__pb2


class BridgeStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Load = channel.unary_unary(
                '/ovm.Bridge/Load',
                request_serializer=api_dot_v1_dot_ovm_dot_bridge__pb2.LoadRequest.SerializeToString,
                response_deserializer=api_dot_v1_dot_ovm_dot_bridge__pb2.LoadResponse.FromString,
                _registered_method=True)
        self.Log = channel.unary_unary(
                '/ovm.Bridge/Log',
                request_serializer=api_dot_v1_dot_ovm_dot_bridge__pb2.LogRequest.SerializeToString,
                response_deserializer=api_dot_v1_dot_ovm_dot_bridge__pb2.LogResponse.FromString,
                _registered_method=True)
        self.Submit = channel.unary_unary(
                '/ovm.Bridge/Submit',
                request_serializer=api_dot_v1_dot_ovm_dot_bridge__pb2.SubmitRequest.SerializeToString,
                response_deserializer=api_dot_v1_dot_ovm_dot_bridge__pb2.SubmitResponse.FromString,
                _registered_method=True)


class BridgeServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Load(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Log(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Submit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_BridgeServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Load': grpc.unary_unary_rpc_method_handler(
                    servicer.Load,
                    request_deserializer=api_dot_v1_dot_ovm_dot_bridge__pb2.LoadRequest.FromString,
                    response_serializer=api_dot_v1_dot_ovm_dot_bridge__pb2.LoadResponse.SerializeToString,
            ),
            'Log': grpc.unary_unary_rpc_method_handler(
                    servicer.Log,
                    request_deserializer=api_dot_v1_dot_ovm_dot_bridge__pb2.LogRequest.FromString,
                    response_serializer=api_dot_v1_dot_ovm_dot_bridge__pb2.LogResponse.SerializeToString,
            ),
            'Submit': grpc.unary_unary_rpc_method_handler(
                    servicer.Submit,
                    request_deserializer=api_dot_v1_dot_ovm_dot_bridge__pb2.SubmitRequest.FromString,
                    response_serializer=api_dot_v1_dot_ovm_dot_bridge__pb2.SubmitResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ovm.Bridge', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('ovm.Bridge', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class Bridge(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Load(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ovm.Bridge/Load',
            api_dot_v1_dot_ovm_dot_bridge__pb2.LoadRequest.SerializeToString,
            api_dot_v1_dot_ovm_dot_bridge__pb2.LoadResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Log(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ovm.Bridge/Log',
            api_dot_v1_dot_ovm_dot_bridge__pb2.LogRequest.SerializeToString,
            api_dot_v1_dot_ovm_dot_bridge__pb2.LogResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)

    @staticmethod
    def Submit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/ovm.Bridge/Submit',
            api_dot_v1_dot_ovm_dot_bridge__pb2.SubmitRequest.SerializeToString,
            api_dot_v1_dot_ovm_dot_bridge__pb2.SubmitResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
