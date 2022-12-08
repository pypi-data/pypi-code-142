from djangoldp.views import LDPViewSet
from ..models import NeedleActivity
import logging
from djangoldp_account.models import LDPUser


class NeedleActivityViewset(LDPViewSet):
    # TODO: check change only read
    pass


def create_welcome_needle_activity(user):
    logging.error("create_welcome_needle_activity")
    welcome = NeedleActivity(title="Welcome", content="Welcome", creator=user)
    welcome.save()

    logging.error("welcome")
