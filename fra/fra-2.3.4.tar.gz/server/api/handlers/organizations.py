import os
from uuid import UUID

import flask_rebar

from motor.models import UserModel
from motor.models import UserOrganization
from organizations.models import OrganizationModel
from server.config import basedir
from server.database import db
from server.rebar import registry
from server.schemas.organization import OrganizationResponseSchema
from server.schemas.organization import OrganizationSchema
from server.schemas.organization import OrganizationUsersListResponseSchema


@registry.handles(
    rule="/organization",
    method="POST",
    request_body_schema=OrganizationSchema(),
    response_body_schema={201: OrganizationResponseSchema()},
)
def create_organization():
    """
    Creates an organization and returns it's uuid
    """
    body = flask_rebar.get_validated_body()
    organization = OrganizationModel(**body)
    db.session.add(organization)
    db.session.commit()
    path = os.path.join(basedir, "uploads", str(organization.id))
    os.makedirs(path)
    return organization, 201


@registry.handles(
    rule="/organization/<uuid:organization_id>",
    method="GET",
    response_body_schema={200: OrganizationResponseSchema()},
)
def get_organization(organization_id: UUID):
    """
    Return an organization by id
    """
    organization = OrganizationModel.query.filter_by(id=organization_id).first_or_404()
    return organization


@registry.handles(
    rule="/organization/<uuid:organization_id>/users",
    method="GET",
    response_body_schema={200: OrganizationUsersListResponseSchema()},
)
def get_organization_users(organization_id: UUID):
    """
    Return all the users in the organization
    """
    organization_users = UserOrganization.query.filter_by(
        organization_id=organization_id
    ).all()
    users_ids = [user.user_id for user in organization_users]
    users = UserModel.query.filter_by(UserModel.id.in_(users_ids)).all()
    return users, 200
