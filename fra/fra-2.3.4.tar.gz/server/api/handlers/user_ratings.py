from uuid import UUID

import flask_rebar

from motor.adaptors import request_process_recommendations
from motor.models import UserModel
from motor.models import UserOrganization
from motor.models import UserRating
from server.database import db
from server.rebar import registry
from server.schemas.general import UserSchemaRequest
from server.schemas.general import UserSchemaResponse
from server.schemas.user_ratings import UserRatingListResponseSchema
from server.schemas.user_ratings import UserRatingResponseSchema
from server.schemas.user_ratings import UserRatingSchema


@registry.handles(
    rule="/organization/<uuid:organization_id>/user/rating",
    method="POST",
    request_body_schema=UserRatingSchema(),
    response_body_schema={201: UserRatingResponseSchema()},
)
def user_rating(organization_id: UUID):
    """
    Saves user ratings for later being use for getting recommendations
    """
    body = flask_rebar.get_validated_body()
    user_rating = UserRating(**body)
    db.session.add(user_rating)
    db.session.commit()
    ratings = UserRating.query.filter_by(
        organization_id=organization_id, user_id=body["user_id"]
    ).all()
    if ratings is not None and len(ratings) > 3:
        request_process_recommendations(
            user_id=body["user_id"], organization_id=organization_id
        )
    return user_rating, 201


@registry.handles(
    rule="/organization/<uuid:organization_id>/user/<uuid:user_id>/ratings",
    method="GET",
    response_body_schema=UserRatingListResponseSchema(),
)
def get_user_rating(organization_id: UUID, user_id: UUID):
    """
    Get list of saved ratings by user
    """
    user_ratings = UserRating.query.filter_by(
        user_id=user_id, organization_id=organization_id
    ).all()

    return user_ratings


@registry.handles(
    rule="/organization/<uuid:organization_id>/user",
    method="POST",
    request_body_schema=UserSchemaRequest(),
    response_body_schema={201: UserSchemaResponse()},
)
def create_user(organization_id: UUID):
    """
    Creates an user and returns the user's uuid
    """
    body = flask_rebar.get_validated_body()
    user = UserModel(**body)
    db.session.add(user)
    db.session.commit()
    user_organization = UserOrganization(
        organization_id=organization_id, user_id=user.id
    )
    db.session.add(user_organization)
    db.session.commit()

    return user, 201
