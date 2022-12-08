from file_transfer.controllers.base_controller import BaseController
from file_transfer.services.base_service import BaseService

from file_transfer.models.request import Request

from file_transfer.factories.base_factory import BaseFactory

#Infra
from file_transfer.infra.s3_downloader.s3_downloader import S3Downloader 
from file_transfer.infra.local_downloader.local_downloader import LocalDownloader 


from file_transfer.infra.s3_file_saver.s3_file_saver import S3FileSaver 
from file_transfer.infra.pure_file_saver.pure_file_saver import PureFileSaver 
from file_transfer.infra.local_file_saver.local_file_saver import LocalFileSaver 

from file_transfer.infra.compresser.zip_compresser import ZipCompresser


#Services
from file_transfer.services.downloader_service import DownloaderService
from file_transfer.services.uploader_service import UploaderService



#Controllers
from file_transfer.controllers.downloader_controller import  DownloaderController 
from file_transfer.controllers.uploader_controller import  UploaderController 


from file_transfer.utils.helpers import *


class Factory(BaseFactory):
   
  
    def __init__(self, request: Request):
        super().__init__(request)



    def make_downloader(self, script_name, general_config, script_config):
        

            if ('downloader' not in script_config):
                raise Exception('downloader configuration key is required')

            downloader_type = script_config['downloader']['type']

            script_config['downloader'] = { **script_config['downloader'], 'temp_directory': get_attr(script_config,'temp_directory','/tmp') }
            

            if (downloader_type == 's3'):
                return S3Downloader(script_config['downloader'])

            if (downloader_type == 'local'):
                return LocalDownloader(script_config['downloader'])

            else:
                raise Exception(f'Downloader type not implemented: {downloader_type}')    
    
    def make_compresser(self, script_name, general_config, script_config):
        return  ZipCompresser(script_config)

    def make_saver(self, script_name, general_config, script_config):
       
            if ('saver' not in script_config):
                raise Exception('saver configuration key is required')

            saver_type = script_config['saver']['type']

            script_config['saver'] = { **script_config['saver'], 'temp_directory': get_attr(script_config,'temp_directory','/tmp') }
            

            if (saver_type == 's3'):
                return S3FileSaver(script_config['saver'])  

            elif (saver_type == 'local'):
                return LocalFileSaver(script_config['saver'])  

            elif (saver_type == 'download'):
                script_config['compress'] = True
                return PureFileSaver(script_config['saver'])          
            else:    
                raise Exception(f'Saver type not implemented: {saver_type}')    
        

    def make_service(self, script_name, general_config, script_config) -> BaseService:
        
        script_config = script_config['config']
        
        compresser = self.make_compresser(script_name, general_config, script_config)

        if (script_name == 'download'):
            downloader = self.make_downloader(script_name, general_config, script_config)
            return DownloaderService(script_config, downloader)
        elif (script_name == 'upload'):
            saver = self.make_saver(script_name, general_config, script_config)
            return UploaderService(script_config, saver, compresser)  
        else:
            raise Exception('Service not implemented')      
       



    def make_controller(self) -> BaseController:
        
        route = self.request.route
        script_name = self.get_script_name(route)
        service = self.make_service(script_name, self.general_config, self.script_config)
        
        if (script_name == 'download'):
           controller = DownloaderController(self.request, service)
        elif (script_name == 'upload'):
           controller = UploaderController(self.request, service)
        else:
            raise Exception('Controller not implemented')  
        
        return controller     



        

    
    