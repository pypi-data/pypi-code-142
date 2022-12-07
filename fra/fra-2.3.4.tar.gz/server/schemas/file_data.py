from flask_rebar import RequestSchema
from flask_rebar import ResponseSchema
from marshmallow import fields


class FileMapSchema(RequestSchema):
    """
    Load file related data
    """

    data_columns = fields.List(fields.String())
    title_column = fields.String()
    data_separator = fields.String()
    id_column = fields.String()
    file_id = fields.UUID()


class FileMapResponseSchema(ResponseSchema):
    file_id = fields.UUID()
