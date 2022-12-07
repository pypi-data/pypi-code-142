from uuid import UUID

from motor.processor import main
from server.app import make_celery

celery = make_celery()


@celery.task(name="motor.tasks.process_recommendations")
def process_recommendations(user_uid: UUID, organization_id: UUID):
    # check the number of data before requesting process recommendations
    main(user_uid=user_uid, organization_id=organization_id)
