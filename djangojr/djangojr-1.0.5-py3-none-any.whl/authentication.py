from functools import wraps
from .serializer import JsonSerializer as Js
from .token.models import Token
from django.contrib.auth.models import AnonymousUser


def token_authentication(authentication: bool = True):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            request = args[0]
            token = request.META.get("HTTP_AUTHORIZATION")
            if token:
                try:
                    token = Token.objects.get(token=token)
                    request.user = token.user
                except Token.DoesNotExist:
                    token = None
            if not token:
                request.user = AnonymousUser()
                if authentication and not request.user.is_authenticated:
                    return Js.http_401_unauthorized()
            return func(*args, **kwargs)
        return wrapper
    return decorator
