import logging

from .conf import config
from .router import router
from .rules import front_door_check_access
from .utils import get_client_ip

logger = logging.getLogger(__name__)


class FrontDoorMiddleware:
    def __init__(self, get_response=None):
        self.get_response = get_response
        if config.ENABLED:
            logger.debug(f"FrontDoor enabled. Policy: {config.DEFAULT_POLICY_LABEL}")
        else:
            logger.debug("FrontDoor disabled")

    def __call__(self, request):
        ip = get_client_ip(request)
        request.user_ip = ip
        if front_door_check_access(request):
            response = self.get_response(request)
        else:
            response = router.route(request)
        return response
