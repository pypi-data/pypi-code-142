from django.contrib.auth.models import Permission, Group
from functools import wraps
from .serializer import JsonSerializer as Js


def has_permission(permissions: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = args[0].user
            if not user.is_superuser:
                user_permissions = Permission.objects.filter(
                    user=user).values_list("codename", flat=True)
                for p in permissions:
                    if p not in user_permissions:
                        return Js.http_403_forbidden()
            return func(*args, **kwargs)
        return wrapper
    return decorator


def has_group(groups: list):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            user = args[0].user
            if not user.is_superuser:
                user_groups = Group.objects.filter(
                    user=user).values_list("name", flat=True)
                for g in groups:
                    if g not in user_groups:
                        return Js.http_403_forbidden()
            return func(*args, **kwargs)
        return wrapper
    return decorator
