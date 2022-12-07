import json
from uuid import UUID

from motor.models import RecommendationsModel
from server.rebar import registry


@registry.handles(
    rule="/organization/<uuid:organization_id>/recommendations/<uuid:user_uid>",
    method="GET",
)
def get_recommendations(organization_id: UUID, user_uid: UUID):
    """
    Process and returns recommendations for an user, based on the ratings saved via /api/user/rating
    """
    recommendations = RecommendationsModel.query.filter_by(
        organization_id=organization_id, user_id=user_uid
    ).first()
    # instead of 404, return a message saying not enough data for get recommendations
    if recommendations is None:
        return {"msg": "Not enough data for get recommendations, try it later"}, 200
    return json.loads(recommendations.recommendations), 201
