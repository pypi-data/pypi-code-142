from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.exceptions import ImproperlyConfigured
from django.db import models
from django.utils.module_loading import import_string

from .consts import Status, Type

User = get_user_model()

EMAIL_MAX_LENGTH = 256
TYPE_MAX_LENGTH = 30


def get_type_choices():
    TYPE_CHOICES_PATH = getattr(settings, "TYPE_CHOICES_PATH", None)

    if TYPE_CHOICES_PATH:
        try:
            types = import_string(TYPE_CHOICES_PATH)
        except ImportError:
            raise ImproperlyConfigured("module cannot be resolved.")

        return types.choices
    else:
        return Type.choices


class Ticket(models.Model):
    email = models.EmailField(max_length=EMAIL_MAX_LENGTH)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    status = models.CharField(
        max_length=8, choices=Status.choices, default=Status.NEW
    )
    type = models.CharField(
        max_length=TYPE_MAX_LENGTH,
        choices=get_type_choices(),
        default=Type.INFO,
    )

    def __str__(self):
        return "{}, {}, {}".format(self.email, self.date, self.description)
