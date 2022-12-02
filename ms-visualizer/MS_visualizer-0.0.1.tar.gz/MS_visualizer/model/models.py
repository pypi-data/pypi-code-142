from datetime import datetime
from pony.orm import *


db = Database()


class Filter(db.Entity):
    id = PrimaryKey(int, auto=True)
    min_x = Required(float)
    max_x = Required(float)
    min_z = Required(float)
    max_z = Required(float)
    min_y = Required(float)
    max_y = Required(float)
    min_intensity = Required(int, unsigned=True)
    x_axis_label = Required(str)
    y_axis_label = Required(str)
    z_axis_label = Required(str)
    path_to_data_folder = Required(str)
    multicharge_region_equation = Optional(str)
    evaluation = Required('Evaluation')


class Algorithm(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str, unique=True)
    description = Optional(str)
    scheme_path = Required(str)
    loading_path = Required(str)
    evaluations = Set('Evaluation')


class User(db.Entity):
    id = PrimaryKey(int, auto=True)
    name = Required(str)
    password = Optional(str)
    evaluations = Set('Evaluation')


class Evaluation(db.Entity):
    id = PrimaryKey(int, auto=True)
    score = Optional(int, size=8, unsigned=True)
    created = Optional(datetime)
    algorithm = Required(Algorithm)
    algorithm_settings = Optional(Json)
    user = Required(User)
    filter = Optional(Filter)
    comment = Optional(LongStr)
    extras = Optional(Json)



db.bind(**{
    'provider': 'sqlite',
    'filename': 'database.sqlite',
    'create_db': True
})
db.generate_mapping(create_tables=True)
