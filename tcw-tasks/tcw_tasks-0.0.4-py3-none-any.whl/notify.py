import os
import sys
import logging
from tcw.database import session, init_engine
from tcw.utils import expired_contests
from tcw.apps.contest.models import Contest
from tcw_tasks.models import Message
from sendgrid import SendGridAPIClient


# globals #
logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s|%(name)s|%(levelname)s|%(message)s'
)

def main():
    uri = os.getenv('SQLALCHEMY_DATABASE_URI', None)
    if not uri:
        logger.error('Must have SQLALCHEMY_DATABASE_URI environment var')
        sys.exit(1)

    init_engine(uri)
    finish_contests()


def finish_contests():
    try:
        contests = expired_contests()
        logger.info("%d contests pending closure" % len(contests))
    except:
        logger.info("No contests pending closure")
        return

    for c in contests:
        try:
            winners = c.pick_winners()
            notify_owner(c, winners)
            logger.info("Closing contest %s (%s)" % (c.name, c.title))
            session.delete(c)
            session.commit()
        except Exception as x:
            logger.warning(x)
            session.rollback()


def notify_owner(contest, winners):
    msg = Message(contest=contest, winners=winners).get_message()
    client = SendGridAPIClient(os.getenv('SENDGRID_API_KEY'))
    response = client.send(message=msg)
    logger.info("Owner notified successfully" % contest.email)


if __name__ == '__main__':
    main()
