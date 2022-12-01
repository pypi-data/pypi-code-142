# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from speechly.slu.v1 import batch_api_pb2 as speechly_dot_slu_dot_v1_dot_batch__api__pb2


class BatchAPIStub(object):
  """Run SLU operations on audio sources without actively waiting the results.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.ProcessAudio = channel.stream_unary(
        '/speechly.slu.v1.BatchAPI/ProcessAudio',
        request_serializer=speechly_dot_slu_dot_v1_dot_batch__api__pb2.ProcessAudioRequest.SerializeToString,
        response_deserializer=speechly_dot_slu_dot_v1_dot_batch__api__pb2.ProcessAudioResponse.FromString,
        )
    self.QueryStatus = channel.unary_unary(
        '/speechly.slu.v1.BatchAPI/QueryStatus',
        request_serializer=speechly_dot_slu_dot_v1_dot_batch__api__pb2.QueryStatusRequest.SerializeToString,
        response_deserializer=speechly_dot_slu_dot_v1_dot_batch__api__pb2.QueryStatusResponse.FromString,
        )


class BatchAPIServicer(object):
  """Run SLU operations on audio sources without actively waiting the results.
  """

  def ProcessAudio(self, request_iterator, context):
    """Create a new background SLU operation for a single audio source.
    An audio source can be
    - audio chunks sent via repeated ProcessAudioRequests, or
    - URI of a file, reachable from the API
    The response includes an `id` that is used to match the operation to the
    results. A `reference` identifier can also be set.
    The destination can be a webhook URL, in which case the results are posted
    there when they are ready. The payload is an instance of `Operation`.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def QueryStatus(self, request, context):
    """Query the status of a given batch operation.
    If the `ProcessAudioRequest` did not define a `results_uri` as a
    destination, the results are returned in the `QueryStatusResponse`.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_BatchAPIServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'ProcessAudio': grpc.stream_unary_rpc_method_handler(
          servicer.ProcessAudio,
          request_deserializer=speechly_dot_slu_dot_v1_dot_batch__api__pb2.ProcessAudioRequest.FromString,
          response_serializer=speechly_dot_slu_dot_v1_dot_batch__api__pb2.ProcessAudioResponse.SerializeToString,
      ),
      'QueryStatus': grpc.unary_unary_rpc_method_handler(
          servicer.QueryStatus,
          request_deserializer=speechly_dot_slu_dot_v1_dot_batch__api__pb2.QueryStatusRequest.FromString,
          response_serializer=speechly_dot_slu_dot_v1_dot_batch__api__pb2.QueryStatusResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'speechly.slu.v1.BatchAPI', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
