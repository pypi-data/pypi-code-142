from worker.api import Configs
from worker.api.downloader.aio_downloader import FilesDownloader
from worker.api.links_getter import LinksGetter
from worker.api.utils.my_logger import get_struct_logger
from worker.appoint_parser import Parser


def load_new(configs:Configs):

    my_logger = get_struct_logger(__name__)
    my_logger.msg('стартуем')

    links_getter = LinksGetter(region_code=configs.REGION_CODE)

    download_links = links_getter.download_links(
        destination_path=configs.LINKS_N_FILES_INFO)

    files_loader = FilesDownloader(
        result_folder=configs.RAW_FILES_FOLDER,
        links_to_load=download_links,
        failed_links_file=configs.LINKS_FAILED_AT_DOWNLOADING,
        meta_data_file=configs.LINKS_N_FILES_INFO
    )
    files_loader.go()

    # удаляем папку с ссылками и метаданными файлов
    # os.removedir(shutil.rmtree(configs.LINKS_FOLDER))

    parser = Parser(configs.SEARCH_WORD)
    return parser.parse_folder(configs.RAW_FILES_FOLDER, 'result.json')


