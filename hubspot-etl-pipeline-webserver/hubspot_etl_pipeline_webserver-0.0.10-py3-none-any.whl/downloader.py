import os, glob
import zipfile

from . import hubspot_helper
from . import bigquery_helper

from threading import Thread

from super_eureka import logging

def get_last_downloaded_zip_file(downloads_folder: str) -> str:
    glob_expr = os.path.join(downloads_folder, '*.zip')
    glob_files = glob.glob(glob_expr)
    files = list(filter(os.path.isfile, glob_files))

    if len(files) == 0:
        return ''

    files.sort(key=lambda x: -os.path.getmtime(x))
    return files[0]

def extract_downloaded_zip_file(downloaded_filepath: str) -> str:
    logging.info(f'Trying to extract report from {downloaded_filepath}.')
    with zipfile.ZipFile(downloaded_filepath, 'r') as zip_file:
        files = zip_file.namelist()
        for entry_file in files:
            if entry_file != 'hubspot-export-summary.csv':
                file_pth = zip_file.extract(entry_file)
                logging.info(f'Extracted as {file_pth}')
                return file_pth
    return ''

def async_download(download_link: str) -> None:
    if not hubspot_helper.download_report(download_link):
        return

    downloads_folder = os.getenv('DOWNLOADS_FOLDER')
    downloaded_filepath = get_last_downloaded_zip_file(downloads_folder)
    if not downloaded_filepath:
        logging.info(f'Could not get last downloaded file from {downloads_folder}. Maybe there are no files there or the folder does not exist.')
        return

    extracted_filepath = extract_downloaded_zip_file(downloaded_filepath)
    if not extracted_filepath:
        logging.info('No report could be found.')
        return
    
    bigquery_helper.submit_for_bigquery(extracted_filepath)
    

def download_and_process(download_link: str) -> None:
    logging.info(f'Starting processing of export from {download_link}')
    thread = Thread(target=async_download, args=(download_link, ))
    thread.start()