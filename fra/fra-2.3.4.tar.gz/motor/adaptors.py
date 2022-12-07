from uuid import UUID


def request_process_recommendations(organization_id: UUID, user_id: UUID):
    from motor.tasks import process_recommendations

    process_recommendations.delay(user_uid=user_id, organization_id=organization_id)
