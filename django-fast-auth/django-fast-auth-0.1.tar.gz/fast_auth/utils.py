from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


def is_email(value):
    if '@' in value:
        return True
    else:
        return False