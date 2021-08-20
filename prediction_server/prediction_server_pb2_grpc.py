# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import prediction_server_pb2 as prediction__server__pb2


class PredictionServerStub(object):
    """option java_multiple_files = true;
    option java_package = "io.grpc.examples.helloworld";
    option java_outer_classname = "HelloWorldProto";
    option objc_class_prefix = "HLW";

    package helloworld;

    The greeting service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ping = channel.unary_unary(
                '/PredictionServer/ping',
                request_serializer=prediction__server__pb2.PingRequest.SerializeToString,
                response_deserializer=prediction__server__pb2.PingResponse.FromString,
                )
        self.predict = channel.unary_unary(
                '/PredictionServer/predict',
                request_serializer=prediction__server__pb2.PredictionRequest.SerializeToString,
                response_deserializer=prediction__server__pb2.PredictionResponse.FromString,
                )


class PredictionServerServicer(object):
    """option java_multiple_files = true;
    option java_package = "io.grpc.examples.helloworld";
    option java_outer_classname = "HelloWorldProto";
    option objc_class_prefix = "HLW";

    package helloworld;

    The greeting service definition.
    """

    def ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def predict(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_PredictionServerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ping': grpc.unary_unary_rpc_method_handler(
                    servicer.ping,
                    request_deserializer=prediction__server__pb2.PingRequest.FromString,
                    response_serializer=prediction__server__pb2.PingResponse.SerializeToString,
            ),
            'predict': grpc.unary_unary_rpc_method_handler(
                    servicer.predict,
                    request_deserializer=prediction__server__pb2.PredictionRequest.FromString,
                    response_serializer=prediction__server__pb2.PredictionResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'PredictionServer', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class PredictionServer(object):
    """option java_multiple_files = true;
    option java_package = "io.grpc.examples.helloworld";
    option java_outer_classname = "HelloWorldProto";
    option objc_class_prefix = "HLW";

    package helloworld;

    The greeting service definition.
    """

    @staticmethod
    def ping(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PredictionServer/ping',
            prediction__server__pb2.PingRequest.SerializeToString,
            prediction__server__pb2.PingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def predict(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/PredictionServer/predict',
            prediction__server__pb2.PredictionRequest.SerializeToString,
            prediction__server__pb2.PredictionResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
