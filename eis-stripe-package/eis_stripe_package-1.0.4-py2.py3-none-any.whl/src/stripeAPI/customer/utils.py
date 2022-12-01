from common.constants.stripe_exceptions_constants import GENERATE_FULL_NAME, STRIPE_GENERIC
from common.exception_service.custom_exception_handler import CoreGenericException


def generate_full_name(first_name: str = None, last_name: str = None):
    try:
        if first_name and last_name:
            return "{0} {1}".format(first_name.strip(), last_name.strip())
        elif first_name:
            return first_name.strip()
        elif last_name:
            return last_name.strip()
        else:
            return None

    except Exception as exception:
        raise CoreGenericException(exception_code=STRIPE_GENERIC,
                                    exception_traceback=exception,
                                    method_name=GENERATE_FULL_NAME)