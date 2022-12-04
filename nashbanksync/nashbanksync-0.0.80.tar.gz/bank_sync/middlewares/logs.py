from ast import literal_eval
from bank_sync.models import RequestLogs, ResponseLogs
import threading
from django.db import connection

class APILogsMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        # Confirm the path requested
        if len(request.path.split("/"))>2:
            # confirm that this is not the django admin page path
            if request.path.split("/")[1] != 'admin':
                threading.Thread(target=self.log_request,
                                args=[request]).start()

        response = self.get_response(request)
        # Code to be executed for each request/response after
        # the view is called.
        
        # Confirm the path requested
        if len(request.path.split("/"))>2:
            # confirm that this is not the django admin page path
            if request.path.split("/")[1] != 'admin':
                threading.Thread(target=self.log_response,
                                    args=[response,request.headers.get("Host", "")]).start()

        return response

    def log_request(self, request):
        request_logs = None
        try:
            request_logs = RequestLogs.objects.create(
                ip=request.headers.get("Host", ""),
                method=request.method,
                path=request.path,
                content_type=request.content_type,
                content_params=request.content_params,
                headers=dict(request.headers),
                user=str(request.user)
            )

            if len(request.body):
                request_logs.body = literal_eval(request.body.decode("utf-8").replace("false","False").replace("true","True").replace("null","None"))
                request_logs.save()
        except Exception as e:
            if request_logs is not None:
                request_logs.error = e
                request_logs.save()
        
        connection.close()

    def log_response(self, response, ip):  
        response_logs = None      
        try:
            response_logs = ResponseLogs.objects.create(ip=ip,headers=dict(response.headers))
            if len(response.data):
                response_logs.content = response.data
                response_logs.save()
        except Exception as e:
            if response_logs is not None:
                response_logs.error = e
                response_logs.save()
        
        connection.close()
