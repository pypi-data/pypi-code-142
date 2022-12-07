from marshmallow import fields
from marshmallow import Schema


class GeneralStatusSchema(Schema):
    status = fields.String()


class UserSchemaRequest(Schema):
    name = fields.String()


class UserSchemaResponse(Schema):
    id = fields.UUID()
    name = fields.String()
