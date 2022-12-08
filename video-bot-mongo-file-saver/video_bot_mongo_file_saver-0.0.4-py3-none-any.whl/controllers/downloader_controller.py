from file_saver.services.base_service import BaseService

from file_saver.models.request import Request
from file_saver.controllers.base_controller import BaseController


class DownloaderController(BaseController):

    def __init__(self, request: Request, service: BaseService):
        super().__init__(request, service)

    def handle(self):
        if (self.service):
            return self.service.execute()
  



        

    
    