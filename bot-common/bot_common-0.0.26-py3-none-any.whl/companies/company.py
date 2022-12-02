from bot_common.utils.utils import catch_exception
from bot_common.utils.db_utils import DbConfig, db_connect, create_table_if_not_exists
from bot_common.companies.company_model import config_headers as headers
from bot_common.utils.logging_conf import logger
from pydantic import BaseModel
import json

configurations_table_name = 'configurations'


@catch_exception
def dict_parser(d: dict):
    parsed_dict = dict()
    for key, val in d.items():
        try:
            val_p = json.loads(val) if isinstance(val, str) else val
        except json.JSONDecodeError:
            val_p = val
        parsed_dict[key] = val_p
    return {k: v for k, v in parsed_dict.items() if v is not None}


class GenericObj(BaseModel):
    def __init__(self, d: dict):
        self.__dict__.update(dict_parser(d))


class Company:
    def __init__(self, field: str, value, db_config: DbConfig):
        self.field = field
        self.value = value
        self.tab_name = configurations_table_name
        self.db, self.cursor = db_connect(db_config)
        create_table_if_not_exists(self.db, self.cursor, self.tab_name, headers)

    @catch_exception
    def get_config(self, opened=True):
        # get config values
        where_active_field = ''
        if opened:
            where_active_field = 'AND is_active = 1'

        get_config_query = f"SELECT * FROM {self.tab_name} WHERE {self.field} LIKE '%{self.value}%' {where_active_field};"
        self.cursor.execute(get_config_query)
        conf_vals = self.cursor.fetchall()
        if not conf_vals:
            self.db.close()
            raise Exception(f'{self.field} {self.value} unexisting or disabled')
        elif len(conf_vals) > 1:
            self.db.close()
            raise Exception(f'{self.field} {self.value} ambiguous or duplicated')

        # get config structure
        get_structure_query = f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = '{self.tab_name}' ORDER BY ordinal_position;"
        self.cursor.execute(get_structure_query)
        structure = self.cursor.fetchall()
        self.db.close()
        # flatten the structure list
        structure = list(sum(structure, ()))
        # remove duplicates from structure_result while keeping the order
        structure = list(dict.fromkeys(structure))
        config_dict = dict(zip(structure[1:], conf_vals[0][1:]))
        return GenericObj(config_dict)


class CompanyManager:
    def __init__(self, db_config: DbConfig, company: str = ''):
        self.company = company
        self.tab_name = configurations_table_name
        self.db, self.cursor = db_connect(db_config)
        create_table_if_not_exists(self.db, self.cursor, self.tab_name, headers)

    @catch_exception
    def get_companies(self, opened=True):
        where_active_field = ''
        if opened:
            where_active_field = 'WHERE is_active = 1'

        get_companies_query = f"SELECT company FROM {self.tab_name} {where_active_field};"
        self.cursor.execute(get_companies_query)
        companies = self.cursor.fetchall()
        self.db.close()
        return [el[0] for el in companies]

    @catch_exception
    def disable_company(self):
        disable_config_query = f"UPDATE {self.tab_name} SET is_active = 0 WHERE company = '{self.company}';"
        self.cursor.execute(disable_config_query)
        self.db.commit()
        logger.info(f'>> disabled {self.company} company')
        self.db.close()

    @catch_exception
    def activate_company(self):
        activate_config_query = f"UPDATE {self.tab_name} SET is_active = 1 WHERE company = '{self.company}';"
        self.cursor.execute(activate_config_query)
        self.db.commit()
        logger.info(f'>> activated {self.company} company')
        self.db.close()
