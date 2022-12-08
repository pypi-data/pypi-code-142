from file_transfer.services.base_service import BaseService

from file_transfer.models.request import Request
from file_transfer.controllers.base_controller import BaseController

from file_transfer.utils.helpers import get_attr

class UploaderController(BaseController):

    def __init__(self, request: Request, service: BaseService):
        super().__init__(request, service)

    def handle(self):
        if (self.service):
            files = self.request.body['script_config']['config']['saver']['data']
            return self.service.execute(files)
  



        

    
    