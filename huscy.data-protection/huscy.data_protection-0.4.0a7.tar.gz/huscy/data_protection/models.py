import enum

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from huscy.subjects.models import Contact


class Request(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name=_('Contact'))

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT,
                                verbose_name=_('Creator'))
    created_at = models.DateTimeField(_('Created at'), auto_now_add=True)

    class Meta:
        abstract = True


class DataAccessRequest(Request):
    class Meta:
        verbose_name = _('Data access request')
        verbose_name_plural = _('Data access requests')


class DataRevocationRequest(Request):
    class TYPES(enum.Enum):
        all_data = (0, _('All data'))
        contact_data = (1, _('Contact data'))

        @classmethod
        def get_value(cls, member):
            return cls[member].value[0]

    type = models.PositiveSmallIntegerField(_('Type'), choices=[x.value for x in TYPES])

    class Meta:
        verbose_name = _('Data revocation request')
        verbose_name_plural = _('Data revocation requests')
