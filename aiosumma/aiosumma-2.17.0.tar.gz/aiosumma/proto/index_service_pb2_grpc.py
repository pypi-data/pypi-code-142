# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import index_service_pb2 as index__service__pb2


class IndexApiStub(object):
    """Manages indices
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.alter_index = channel.unary_unary(
                '/summa.proto.IndexApi/alter_index',
                request_serializer=index__service__pb2.AlterIndexRequest.SerializeToString,
                response_deserializer=index__service__pb2.AlterIndexResponse.FromString,
                )
        self.attach_index = channel.unary_unary(
                '/summa.proto.IndexApi/attach_index',
                request_serializer=index__service__pb2.AttachIndexRequest.SerializeToString,
                response_deserializer=index__service__pb2.AttachIndexResponse.FromString,
                )
        self.commit_index = channel.unary_unary(
                '/summa.proto.IndexApi/commit_index',
                request_serializer=index__service__pb2.CommitIndexRequest.SerializeToString,
                response_deserializer=index__service__pb2.CommitIndexResponse.FromString,
                )
        self.create_index = channel.unary_unary(
                '/summa.proto.IndexApi/create_index',
                request_serializer=index__service__pb2.CreateIndexRequest.SerializeToString,
                response_deserializer=index__service__pb2.CreateIndexResponse.FromString,
                )
        self.delete_document = channel.unary_unary(
                '/summa.proto.IndexApi/delete_document',
                request_serializer=index__service__pb2.DeleteDocumentRequest.SerializeToString,
                response_deserializer=index__service__pb2.DeleteDocumentResponse.FromString,
                )
        self.delete_index = channel.unary_unary(
                '/summa.proto.IndexApi/delete_index',
                request_serializer=index__service__pb2.DeleteIndexRequest.SerializeToString,
                response_deserializer=index__service__pb2.DeleteIndexResponse.FromString,
                )
        self.get_indices_aliases = channel.unary_unary(
                '/summa.proto.IndexApi/get_indices_aliases',
                request_serializer=index__service__pb2.GetIndicesAliasesRequest.SerializeToString,
                response_deserializer=index__service__pb2.GetIndicesAliasesResponse.FromString,
                )
        self.get_index = channel.unary_unary(
                '/summa.proto.IndexApi/get_index',
                request_serializer=index__service__pb2.GetIndexRequest.SerializeToString,
                response_deserializer=index__service__pb2.GetIndexResponse.FromString,
                )
        self.get_indices = channel.unary_unary(
                '/summa.proto.IndexApi/get_indices',
                request_serializer=index__service__pb2.GetIndicesRequest.SerializeToString,
                response_deserializer=index__service__pb2.GetIndicesResponse.FromString,
                )
        self.index_document_stream = channel.stream_unary(
                '/summa.proto.IndexApi/index_document_stream',
                request_serializer=index__service__pb2.IndexDocumentStreamRequest.SerializeToString,
                response_deserializer=index__service__pb2.IndexDocumentStreamResponse.FromString,
                )
        self.index_document = channel.unary_unary(
                '/summa.proto.IndexApi/index_document',
                request_serializer=index__service__pb2.IndexDocumentRequest.SerializeToString,
                response_deserializer=index__service__pb2.IndexDocumentResponse.FromString,
                )
        self.merge_segments = channel.unary_unary(
                '/summa.proto.IndexApi/merge_segments',
                request_serializer=index__service__pb2.MergeSegmentsRequest.SerializeToString,
                response_deserializer=index__service__pb2.MergeSegmentsResponse.FromString,
                )
        self.set_index_alias = channel.unary_unary(
                '/summa.proto.IndexApi/set_index_alias',
                request_serializer=index__service__pb2.SetIndexAliasRequest.SerializeToString,
                response_deserializer=index__service__pb2.SetIndexAliasResponse.FromString,
                )
        self.vacuum_index = channel.unary_unary(
                '/summa.proto.IndexApi/vacuum_index',
                request_serializer=index__service__pb2.VacuumIndexRequest.SerializeToString,
                response_deserializer=index__service__pb2.VacuumIndexResponse.FromString,
                )


class IndexApiServicer(object):
    """Manages indices
    """

    def alter_index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def attach_index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def commit_index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def create_index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete_document(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def delete_index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_indices_aliases(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get_indices(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def index_document_stream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def index_document(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def merge_segments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def set_index_alias(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def vacuum_index(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_IndexApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'alter_index': grpc.unary_unary_rpc_method_handler(
                    servicer.alter_index,
                    request_deserializer=index__service__pb2.AlterIndexRequest.FromString,
                    response_serializer=index__service__pb2.AlterIndexResponse.SerializeToString,
            ),
            'attach_index': grpc.unary_unary_rpc_method_handler(
                    servicer.attach_index,
                    request_deserializer=index__service__pb2.AttachIndexRequest.FromString,
                    response_serializer=index__service__pb2.AttachIndexResponse.SerializeToString,
            ),
            'commit_index': grpc.unary_unary_rpc_method_handler(
                    servicer.commit_index,
                    request_deserializer=index__service__pb2.CommitIndexRequest.FromString,
                    response_serializer=index__service__pb2.CommitIndexResponse.SerializeToString,
            ),
            'create_index': grpc.unary_unary_rpc_method_handler(
                    servicer.create_index,
                    request_deserializer=index__service__pb2.CreateIndexRequest.FromString,
                    response_serializer=index__service__pb2.CreateIndexResponse.SerializeToString,
            ),
            'delete_document': grpc.unary_unary_rpc_method_handler(
                    servicer.delete_document,
                    request_deserializer=index__service__pb2.DeleteDocumentRequest.FromString,
                    response_serializer=index__service__pb2.DeleteDocumentResponse.SerializeToString,
            ),
            'delete_index': grpc.unary_unary_rpc_method_handler(
                    servicer.delete_index,
                    request_deserializer=index__service__pb2.DeleteIndexRequest.FromString,
                    response_serializer=index__service__pb2.DeleteIndexResponse.SerializeToString,
            ),
            'get_indices_aliases': grpc.unary_unary_rpc_method_handler(
                    servicer.get_indices_aliases,
                    request_deserializer=index__service__pb2.GetIndicesAliasesRequest.FromString,
                    response_serializer=index__service__pb2.GetIndicesAliasesResponse.SerializeToString,
            ),
            'get_index': grpc.unary_unary_rpc_method_handler(
                    servicer.get_index,
                    request_deserializer=index__service__pb2.GetIndexRequest.FromString,
                    response_serializer=index__service__pb2.GetIndexResponse.SerializeToString,
            ),
            'get_indices': grpc.unary_unary_rpc_method_handler(
                    servicer.get_indices,
                    request_deserializer=index__service__pb2.GetIndicesRequest.FromString,
                    response_serializer=index__service__pb2.GetIndicesResponse.SerializeToString,
            ),
            'index_document_stream': grpc.stream_unary_rpc_method_handler(
                    servicer.index_document_stream,
                    request_deserializer=index__service__pb2.IndexDocumentStreamRequest.FromString,
                    response_serializer=index__service__pb2.IndexDocumentStreamResponse.SerializeToString,
            ),
            'index_document': grpc.unary_unary_rpc_method_handler(
                    servicer.index_document,
                    request_deserializer=index__service__pb2.IndexDocumentRequest.FromString,
                    response_serializer=index__service__pb2.IndexDocumentResponse.SerializeToString,
            ),
            'merge_segments': grpc.unary_unary_rpc_method_handler(
                    servicer.merge_segments,
                    request_deserializer=index__service__pb2.MergeSegmentsRequest.FromString,
                    response_serializer=index__service__pb2.MergeSegmentsResponse.SerializeToString,
            ),
            'set_index_alias': grpc.unary_unary_rpc_method_handler(
                    servicer.set_index_alias,
                    request_deserializer=index__service__pb2.SetIndexAliasRequest.FromString,
                    response_serializer=index__service__pb2.SetIndexAliasResponse.SerializeToString,
            ),
            'vacuum_index': grpc.unary_unary_rpc_method_handler(
                    servicer.vacuum_index,
                    request_deserializer=index__service__pb2.VacuumIndexRequest.FromString,
                    response_serializer=index__service__pb2.VacuumIndexResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'summa.proto.IndexApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class IndexApi(object):
    """Manages indices
    """

    @staticmethod
    def alter_index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.IndexApi/alter_index',
            index__service__pb2.AlterIndexRequest.SerializeToString,
            index__service__pb2.AlterIndexResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def attach_index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.IndexApi/attach_index',
            index__service__pb2.AttachIndexRequest.SerializeToString,
            index__service__pb2.AttachIndexResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def commit_index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.IndexApi/commit_index',
            index__service__pb2.CommitIndexRequest.SerializeToString,
            index__service__pb2.CommitIndexResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def create_index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.IndexApi/create_index',
            index__service__pb2.CreateIndexRequest.SerializeToString,
            index__service__pb2.CreateIndexResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete_document(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.IndexApi/delete_document',
            index__service__pb2.DeleteDocumentRequest.SerializeToString,
            index__service__pb2.DeleteDocumentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def delete_index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.IndexApi/delete_index',
            index__service__pb2.DeleteIndexRequest.SerializeToString,
            index__service__pb2.DeleteIndexResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_indices_aliases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.IndexApi/get_indices_aliases',
            index__service__pb2.GetIndicesAliasesRequest.SerializeToString,
            index__service__pb2.GetIndicesAliasesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.IndexApi/get_index',
            index__service__pb2.GetIndexRequest.SerializeToString,
            index__service__pb2.GetIndexResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get_indices(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.IndexApi/get_indices',
            index__service__pb2.GetIndicesRequest.SerializeToString,
            index__service__pb2.GetIndicesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def index_document_stream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_unary(request_iterator, target, '/summa.proto.IndexApi/index_document_stream',
            index__service__pb2.IndexDocumentStreamRequest.SerializeToString,
            index__service__pb2.IndexDocumentStreamResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def index_document(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.IndexApi/index_document',
            index__service__pb2.IndexDocumentRequest.SerializeToString,
            index__service__pb2.IndexDocumentResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def merge_segments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.IndexApi/merge_segments',
            index__service__pb2.MergeSegmentsRequest.SerializeToString,
            index__service__pb2.MergeSegmentsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def set_index_alias(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.IndexApi/set_index_alias',
            index__service__pb2.SetIndexAliasRequest.SerializeToString,
            index__service__pb2.SetIndexAliasResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def vacuum_index(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/summa.proto.IndexApi/vacuum_index',
            index__service__pb2.VacuumIndexRequest.SerializeToString,
            index__service__pb2.VacuumIndexResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
