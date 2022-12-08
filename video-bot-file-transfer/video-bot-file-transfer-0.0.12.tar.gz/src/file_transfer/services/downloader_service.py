from file_transfer.services.base_service import BaseService
from os import path
from file_transfer.utils.helpers import get_attr

class DownloaderService(BaseService):
    
    def __init__(self, config, downloader):

        self.config = config

        #workers
        self.downloader = downloader
        self.temp_directory =   get_attr(self.config,  'temp_directory', 'tmp')
        


    def execute(self):

        downloaded_files = []
        download_results = []
        
        #download files
        download_results, downloaded_files = self.downloader.run()
        

        return download_results, downloaded_files