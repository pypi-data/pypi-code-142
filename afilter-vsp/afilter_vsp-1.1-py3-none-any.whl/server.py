import sys
import grpc
import logging
import argparse
import numpy as np
from io import BytesIO
from concurrent import futures
import tritonclient.grpc as grpcclient
import tritonclient.http as httpclient

from afilter_vsp.protos import afilter_vsp_pb2
from afilter_vsp.protos import afilter_vsp_pb2_grpc
# from afilter_vsp.utils.Mask2polygon import mask2ploy
from afilter_vsp.utils.slide_inference import slide_inference
from afilter_vsp.utils.check_health import HealthServicer, \
     _Watcher, _watcher_to_send_response_callback_adapter

try:
    from mmseg.datasets.vsp import VSPDataset
    CLASSES = VSPDataset.CLASSES
except Exception as e:
    CLASSES = ('background', 'island', 'nick', 'open', 'protrusion', 'short')

OK = True
NG = False

def get_class_mask(defect):
    classes = np.array(CLASSES)

    class_mask = []
    for label, name in enumerate(classes):
        if label != 0 and name != '':
            table = [0]*256
            table[label] = 1
            mask = defect.point(table, '1')
            if mask.getextrema() != (0, 0):
                print('[{}]: {}'.format(label, name))
                mask_bytes = BytesIO()
                mask.save(mask_bytes, format='png')
                mask_Onemat = afilter_vsp_pb2.Onemat(rows=mask.size[1], cols=mask.size[0],\
                    d_type=0, mat_data=mask_bytes.getvalue())
                class_mask.append(afilter_vsp_pb2.Onedefect(name=name, mask=mask_Onemat))

    return class_mask

def get_OKNG(defect):
    class_mask = get_class_mask(defect)
    if isinstance(class_mask, list) and len(class_mask) == 0:
        return afilter_vsp_pb2.OneReply(ok_ng=OK)
    else:
        return afilter_vsp_pb2.OneReply(ok_ng=NG, defect=class_mask)

class Filter_VSPServicer(afilter_vsp_pb2_grpc.Filter_VSPServicer, HealthServicer):
    def __init__(self,
                 protocol,
                 url,
                 model_name,
                 set_async = True):
        self.protocol = protocol
        self.url = url
        self.model_name = model_name
        self.set_async = set_async
        try:
            if self.protocol.lower() == "grpc":
                self.triton_client = grpcclient.InferenceServerClient(url=self.url+':28001')
            else:
                self.triton_client = httpclient.InferenceServerClient(url=self.url+':28000',
                    concurrency=100 if self.set_async == True else 1)
        except Exception as e:
            print("context creation failed: " + str(e))
            sys.exit()

        super(Filter_VSPServicer, self).__init__()

    def FilterFunc(self, requests: afilter_vsp_pb2.FilterRequest, context) -> afilter_vsp_pb2.FilterReply:
        reply = []
        # REQ_NUM = len(requests.request)

        defects = slide_inference(self.protocol.lower(), self.triton_client, self.model_name,
                                           requests.request, out_channels = 1, set_async = True)
        for defect in defects:
            reply.append(get_OKNG(defect))
        return afilter_vsp_pb2.FilterReply(reply=reply)

    def FilterChat(self, requests_iterator, context):
        for request in requests_iterator:
            defects = slide_inference(self.protocol.lower(), self.triton_client, self.model_name,
                                            [request], out_channels = 1, set_async = True)
            for defect in defects:
                yield get_OKNG(defect)
    
    def FilterCheck(self, request, context):
        response = self.Check(request, context)
        if response.status == afilter_vsp_pb2.HealthCheckResponse.SERVING:
            server_live = self.triton_client.is_server_live()
            server_ready = self.triton_client.is_server_ready()
            model_ready = self.triton_client.is_model_ready(self.model_name)
            if server_live and server_ready and model_ready:
                return afilter_vsp_pb2.HealthCheckResponse(status=afilter_vsp_pb2.HealthCheckResponse.SERVING)
            else:
                return afilter_vsp_pb2.HealthCheckResponse(status=afilter_vsp_pb2.HealthCheckResponse.NOT_SERVING)
        else:
            return response

    def FilterWatch(self, request, context, send_response_callback=None):
        blocking_watcher = None
        if send_response_callback is None:
            # The server does not support the experimental_non_blocking
            # parameter. For backwards compatibility, return a blocking response
            # generator.
            blocking_watcher = _Watcher()
            send_response_callback = _watcher_to_send_response_callback_adapter(
                blocking_watcher)
        service = request.service
        with self._lock:
            status = self._server_status.get(service)
            if status is None:
                status = afilter_vsp_pb2.HealthCheckResponse.SERVICE_UNKNOWN  # pylint: disable=no-member
            elif status == afilter_vsp_pb2.HealthCheckResponse.SERVING:
                server_live = self.triton_client.is_server_live()
                server_ready = self.triton_client.is_server_ready()
                model_ready = self.triton_client.is_model_ready(self.model_name)
                if server_live and server_ready and model_ready:
                    status =afilter_vsp_pb2.HealthCheckResponse.SERVING
                else:
                    status =afilter_vsp_pb2.HealthCheckResponse.NOT_SERVING
            send_response_callback(
                afilter_vsp_pb2.HealthCheckResponse(status=status))
            if service not in self._send_response_callbacks:
                self._send_response_callbacks[service] = set()
            self._send_response_callbacks[service].add(send_response_callback)
            context.add_callback(
                self._on_close_callback(send_response_callback, service))
        return blocking_watcher

def afilter_vsp_serve(protocol, url, model_name):
    MAX_MESSAGE_LENGTH = 256*1024*1024 # 256MB
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), options=[
               ('grpc.max_send_message_length', MAX_MESSAGE_LENGTH),
               ('grpc.max_receive_message_length', MAX_MESSAGE_LENGTH)])
    afilter_vsp_pb2_grpc.add_Filter_VSPServicer_to_server(
        Filter_VSPServicer(protocol, url, model_name, set_async = True), server)
    server.add_insecure_port('[::]:50052')
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-u',
        '--triton_url',
        type=str,
        required=False,
        default='localhost',
        help='afilter_vsp server URL. Default is localhost.')
    parser.add_argument('-i',
        '--protocol',
        type=str,
        required=False,
        default='gRPC',
        help='Protocol (HTTP/gRPC) used to communicate with ' +
        'the afilter_vsp service. Default is HTTP.')
    parser.add_argument('-m',
        '--model_name',
        default='segformer-b4',
        help='The model name in the server')
    args = parser.parse_args()

    logging.basicConfig()
    afilter_vsp_serve(args.protocol, args.triton_url, args.model_name)
