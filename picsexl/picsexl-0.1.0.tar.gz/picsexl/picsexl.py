import typing
from datetime import datetime

from .excelwriter.constants import DECLINED_EVENT_RULE
from .excelwriter.excelwriter import ExcelWriter
from .excelwriter.exceptions import ExcelWriterException
from .icsreader.exceptions import ICSReaderException
from .icsreader.icsreader import ICSReader
from .icssniffer.exceptions import ICSSnifferException
from .icssniffer.icssniffer import ICSSniffer

MAIN_HEADERS = [
    "start_date",
    "summary",
    "start_time",
    "end_time",
    "your_status",
    "all_day",
    "end_date",
]


class PIcsExl:
    def __init__(
        self,
        file_path: str,
        mail_to: str,
        start_date: datetime,
        end_date: datetime,
    ):
        self.__file_path: str = file_path
        self.__mail_to: str = mail_to
        self.__start_date: datetime = start_date
        self.__end_date: datetime = end_date
        self.__workbook_name: str = f"{self.__mail_to}-{datetime.isoformat(datetime.now())[:19].replace(':', '-')}"
        self.__ics_sniffer: ICSSniffer = ICSSniffer(
            file_path=self.__file_path,
        )

    def run_sniff_and_write_ics_lines(self) -> str:
        try:
            ics_string: typing.AnyStr = self.__ics_sniffer.get_ics_file_string()
            calendar_parser = ICSReader(
                ics_string=ics_string,
                mail_to=self.__mail_to,
                start_date=self.__start_date,
                end_date=self.__end_date,
            )

            ics_list: typing.List = calendar_parser.get_events_from_ics()
            excel_worker = ExcelWriter(
                workbook_name=f"{self.__ics_sniffer.main_path}/{self.__workbook_name}",
                date_cols=["A", "C", "D", "G"],
                conditional_formatting=[
                    (f"A1:G{len(ics_list) + 1}", DECLINED_EVENT_RULE),
                ],
            )

            if ics_list:
                data_list = []

                headers_list: typing.List = MAIN_HEADERS
                data_list.append(headers_list)

                for data in ics_list:
                    to_append = [data[ih] for ih in headers_list]
                    if to_append not in data_list:
                        data_list.append(to_append)

                excel_worker.fill_workbook(all_data={self.__workbook_name: data_list})

        except ICSSnifferException as e:
            raise PIcsExlException(
                msg="Файловая ошибка. Директория/файл не найден.", exc=e.exc
            )
        except ICSReaderException as e:
            raise PIcsExlException(msg="Ошибка парсинга .ics файла.", exc=e.exc)
        except ExcelWriterException as e:
            raise PIcsExlException(msg="Внутренняя ошибка работы с Excel.", exc=e.exc)
        return self.__workbook_name


class PIcsExlException(Exception):
    def __init__(
        self, exc: typing.Optional[Exception] = None, msg: typing.Optional[str] = None
    ):
        self.exc = exc
        self.msg = msg
