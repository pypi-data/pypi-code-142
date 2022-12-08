from file_transfer.services.base_service import BaseService

from file_transfer.models.request import Request
from file_transfer.controllers.base_controller import BaseController


class DownloaderController(BaseController):

    def __init__(self, request: Request, service: BaseService):
        super().__init__(request, service)

    def handle(self):
        if (self.service):
            return self.service.execute()
  



        

    
    