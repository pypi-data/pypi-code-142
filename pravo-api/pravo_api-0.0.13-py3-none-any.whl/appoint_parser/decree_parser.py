import glob
import json
import os
import warnings
from pathlib import Path
import typing

from bs4 import BeautifulSoup

from .parsers import MultipleAppointment, SingleAppointment
from .utils import models
from .utils.my_logger import get_struct_logger


warnings.filterwarnings("ignore", category=DeprecationWarning)


class PreProcess:
    '''Достает всю инфу о файле'''

    def __init__(self, word_to_search='') -> None:
        self.file_data: models.FileData = None
        self.word_to_search = 'назначить'
        self.logger = get_struct_logger(
            name=__name__, log_file=os.environ['pravo_api_log_file'])

    def get_file_meta_info(self, soup: BeautifulSoup) -> typing.Dict[str, str]:
        my_meta = soup.find('my_meta')
        meta_info = {}
        for key in self.file_data.dict().keys():
            info = my_meta.get(key)
            if info:
                meta_info[key] = info
        return meta_info

    def _get_file_info(self, file_path: str) -> typing.Dict[str, str]:
        file_name = Path(file_path).name
        doc_id = file_name.strip('.hmtl').strip('.txt')
        return {'file_name': file_name, 'file_path': file_path, 'doc_id': doc_id}

    @staticmethod
    def _get_soup(file_path: typing.Union[str, Path]) -> BeautifulSoup:
        with open(file_path, encoding='utf-8') as f:
            raw_text = f.read()
        soup = BeautifulSoup(raw_text, 'html.parser')
        return soup

    def get_raw_text(self, soup: BeautifulSoup) -> typing.Tuple[str, typing.List[str]]:
        '''достает сырой и разделенный на абзцы текст из html'''

        raw_text = soup.get_text('|||', strip=True).split('|||')
        raw_text = [e.replace('\xa0', ' ').replace('Complex', '')
                    for e in raw_text]
        splitted_text_in_lines = [' '.join(e.split()) for e in raw_text]
        fully_raw_text = '\n'.join(splitted_text_in_lines)

        return (fully_raw_text, splitted_text_in_lines)

    def check_keyword_in_raw_text(self, raw_text: str) -> bool:
        if not self.word_to_search:
            return True
        return any((self.word_to_search.lower() in raw_text,
                    self.word_to_search.title() in raw_text))

    def get_all_doc_info(self, file_path: typing.Union[str,Path]) -> models.FileData:

        file_info = self._get_file_info(file_path=file_path)
        self.file_data = models.FileData(**file_info)

        soup = self._get_soup(file_path)
        raw_text, splitted_text = self.get_raw_text(soup)

        if not self.check_keyword_in_raw_text(raw_text):
            self.logger.warning(
                f'в документе нет искомого слова - {self.word_to_search}')
            raise ValueError(
                f'в документе нет искомого слова - {self.word_to_search}')

        meta_data = self.get_file_meta_info(soup=soup)

        self.file_data.text_raw = raw_text
        self.file_data.splitted_text = splitted_text

        if meta_data:
            file_info_dict = self.file_data.dict()
            file_info_dict.update(meta_data)
            self.file_data = models.FileData(**file_info_dict) 

        return self.file_data


class Parser:
    """ main process """

    def __init__(self, word_to_search: str) -> None:
        self.preproc = PreProcess(word_to_search)
        self.file_data = models.FileData()
        self.single_appo_parser = SingleAppointment()
        self.multiple_appo_parser = MultipleAppointment()
        self.logger = get_struct_logger(
            name=__name__, log_file=os.environ['pravo_api_log_file'])
        self.folder_to_parse = ''

    def _delete_html_files(self):
        files = glob.glob(f'{self.folder_to_parse}/*')
        for f in files:
            os.remove(f)
        self.logger.debug('удалили распаршенные html-файлы')

    def determine_if_multiple_appo(self) -> bool:
        '''определяет вид дока и отдает соответствующему классу'''
        for w in ['срок полномочий:', 'летний срок:', 'следующих лиц:']:
            if w in self.file_data.text_raw:
                return True

    def update_parsing_result_file(self, file_data: models.FileData, file_destination: typing.Union[str, Path]):
        '''добавялет в файл результатами парсинга распаршенные данные '''

        file_data = file_data.dict(exclude={'splitted_text', 'naznach_line'})

        try:
            with open(file_destination, 'r', encoding='utf-8') as f:
                existing_data = json.load(f)

        except (json.JSONDecodeError, FileNotFoundError):
            existing_data = {}

        existing_data[file_data['doc_id']] = file_data
        self.save_parsed_file(file_data=existing_data,
                              file_destination=file_destination)

    def save_parsed_file(self, file_data: dict, file_destination: typing.Union[str, Path]):
        with open(file_destination, 'w', encoding='utf-8') as f:
            json.dump(file_data, f, ensure_ascii=False)

    def parse_file(self, file_path: str) -> models.FileData:
        # собрали инфу про файл
        file_with_info = self.preproc.get_all_doc_info(file_path)
        self.file_data = file_with_info
        if self.determine_if_multiple_appo():
            self.logger.debug('видимо, в документе несколько позиций')
            file_with_app_lines = self.multiple_appo_parser.parse(
                self.file_data)
        else:
            self.logger.debug('видимо, в документе одна позиция')
            file_with_app_lines = self.single_appo_parser.parse(self.file_data)

        return file_with_app_lines

    def parse_folder(self, 
                    folder: typing.Union[str, Path], 
                    parsing_results_file: typing.Union[str, Path])->typing.Dict:
        self.folder_to_parse = folder
        parsed_ok = 0
        for file in os.listdir(folder):
            try:
                self.logger = self.logger.bind(doc_id=file)
                parsed_data = self.parse_file(
                    file_path=os.path.join(folder, file))
                self.update_parsing_result_file(
                    file_data=parsed_data, file_destination=parsing_results_file)
                parsed_ok += 1
                self.logger.debug(f'Распарсили и сохранили {file}')
            except ValueError as ex:
                self.logger.warn(str(ex))

        self.logger = self.logger.unbind('doc_id')
        self.logger.debug(
            f'Нашли назначение в {parsed_ok} документах из {len(os.listdir(folder))}')
        self._delete_html_files()



if __name__ == '__main__':
    folder = r'C:\Users\ironb\прогр\Declarator\appointment-parser\pravitelstvo'
    file = '102737677.html'
    path = Path(folder) / file

    parser = Parser(word_to_search='назначить')
    res = parser.parse_file(path)
    print(res)
