from flask_rebar import RequestSchema
from flask_rebar import ResponseSchema
from marshmallow import fields
from marshmallow import pre_dump
from marshmallow import pre_load

from server.schemas.general import UserSchemaResponse


class OrganizationSchema(RequestSchema):
    name = fields.String()


class OrganizationResponseSchema(ResponseSchema):
    id = fields.UUID()
    name = fields.String()


class OrganizationUsersListResponseSchema(ResponseSchema):
    data = fields.Nested(UserSchemaResponse, many=True)

    @pre_dump
    @pre_load
    def envelope_in_data(self, data, **kwargs):
        if type(data) is not dict or "data" not in data.keys():
            return {"data": data}
        else:
            return data
