import dataclasses
import sqlalchemy.sql


@dataclasses.dataclass
class Link:
    source_key: sqlalchemy.Column
    target_key: sqlalchemy.Column


@dataclasses.dataclass
class Many2OneLink(Link):
    pass


@dataclasses.dataclass
class One2ManyLink(Link):
    pass


@dataclasses.dataclass
class Many2ManyLink(Link):
    intermediate_source_key: sqlalchemy.Column
    intermediate_target_key: sqlalchemy.Column
