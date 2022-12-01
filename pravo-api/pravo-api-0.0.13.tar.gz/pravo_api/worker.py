import os
import sys
from pathlib import Path
from typing import Union

from pravo_api.api.downloader.aio_downloader import FilesDownloader
from pravo_api.api.utils.my_logger import get_struct_logger
from pravo_api.api.links_getter import LinksGetter
from pravo_api.appoint_parser import Parser
from pravo_api.api import Configs


class PravoApi:

    def __init__(self, log_file:Union[str, None], parse_appointments=None, **configs) -> None:
        self.parse_appointments = parse_appointments
        self.config = Configs(**configs)
        if log_file:
            log_file = self.get_absolute_filepath(log_file)
        else:
            log_file = str(Path(sys.path[0]) / 'pravo.log')
        os.environ.setdefault('pravo_api_log_file', log_file)
    
    def get(self, output_filename:str=None):
        if output_filename:
            output_filename = self.get_absolute_filepath(output_filename)
        appoints = self._load_new(self.config, output_filename)
        return appoints

    def get_absolute_filepath(self, output_filepath:str)->str:
        """если не абсолютный путь, то сохраняем в место, откуда запускали скрипт"""
        output_filepath = Path(output_filepath)
        if not output_filepath.is_absolute():
            parent_folder = sys.path[0]
            output_filepath = parent_folder / output_filepath
        return str(output_filepath)

    def _load_new(self, configs:Configs, output_filename:str=None):
        my_logger = get_struct_logger(__name__, os.environ['pravo_api_log_file'])
        my_logger.msg('стартуем')

        links_getter = LinksGetter(configs=configs)
        downloaded_links = links_getter.download_links()
            
        files_loader = FilesDownloader(
            result_folder=configs.RAW_FILES_FOLDER,
            links_to_load=downloaded_links,
            failed_links_file=configs.LINKS_FAILED_AT_DOWNLOADING,
            meta_data_file=configs.LINKS_N_FILES_INFO,
            format=configs.SAVE_FORMAT
        )

        files_loader.go()
        
        if self.parse_appointments:
            parser = Parser(configs.SEARCH_WORD)
            return parser.parse_folder(configs.RAW_FILES_FOLDER, output_filename)




