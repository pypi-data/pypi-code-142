from bot_common.utils.utils import catch_exception
from bot_common.utils.db_utils import DbConfig, db_connect
from bot_common.utils.logging_conf import logger
from pydantic import BaseModel
import json

configurations_table_name = 'configurations'


@catch_exception
def get_companies(db_config: DbConfig):
    db, cursor = db_connect(db_config)
    get_companies_query = f"SELECT company FROM {configurations_table_name};"
    cursor.execute(get_companies_query)
    companies = cursor.fetchall()
    db.close()
    return [el[0] for el in companies]


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

    @catch_exception
    def get_config(self):
        # get config values
        get_config_query = f"SELECT * FROM {self.tab_name} WHERE {self.field} LIKE '%{self.value}%';"
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
