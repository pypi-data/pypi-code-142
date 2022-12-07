from flask_rebar import RequestSchema
from flask_rebar import ResponseSchema
from marshmallow import fields
from marshmallow import pre_dump
from marshmallow import pre_load


class UserRatingSchema(RequestSchema):
    """
    Save user ratings (could be notes, prices, times)
    This depending on the recommendation we want to match
    """

    user_id = fields.UUID()
    title = fields.String()
    rating = fields.Float()
    organization_id = fields.UUID()


class UserRatingResponseSchema(ResponseSchema):
    id = fields.UUID()
    user_id = fields.UUID()
    title = fields.String()
    rating = fields.Float()


class UserRatingListResponseSchema(ResponseSchema):
    data = fields.Nested(UserRatingResponseSchema, many=True)

    @pre_dump
    @pre_load
    def envelope_in_data(self, data, **kwargs):
        if type(data) is not dict or "data" not in data.keys():
            return {"data": data}
        else:
            return data
