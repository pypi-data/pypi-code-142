from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

from django_reactions import loaders
from django_reactions.conf import get_settings

Settings = get_settings()

ReactionStatus = loaders.ReactionStatus
ReactionType = loaders.ReactionType

REACTION_CHOICES = ReactionType.choices
REACTION_CHOICE_VALUES = ReactionType.values
REACTION_DEFAULT = ReactionType.get_default()

DJANGO_REACTION_MAX_CHARS = Settings.DJANGO_REACTION_MAX_CHARS


class ReactionQuerySet(models.QuerySet):
    def active(self):
        return self.filter(status=ReactionStatus.ACTIVE)

    def inactive(self):
        return self.filter(status=ReactionStatus.INACTIVE)

    def by_reaction(self, reaction):
        is_value = reaction in REACTION_CHOICE_VALUES
        is_choice = reaction in REACTION_CHOICES
        if not any([is_value, is_choice]):
            raise ValueError(f"Invalid reaction type: {reaction}")
        if is_value:
            reaction = getattr(ReactionType, reaction)
        return self.filter(reaction=reaction)

class ReactionManager(models.Manager):
    def get_queryset(self):
        return ReactionQuerySet(self.model, using=self._db)

    def active(self):
        return self.get_queryset().active()
    
    def inactive(self):
        return self.get_queryset().inactive()
    
    def by_reaction(self, reaction):
        return self.get_queryset().by_reaction(reaction)

class Reaction(models.Model):
    user = models.ForeignKey(Settings.DJANGO_REACTION_USER_MODEL, on_delete=models.CASCADE)
    # Related object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # Field for the type of reaction
    reaction = models.CharField(max_length=DJANGO_REACTION_MAX_CHARS, 
        default=REACTION_DEFAULT, choices=REACTION_CHOICES)

    # Status of the reaction
    status = models.IntegerField(choices=ReactionStatus.choices, default=ReactionStatus.ACTIVE)
    
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = ReactionManager()

    @property
    def is_active(self):
        return self.status == ReactionStatus.ACTIVE

    @property
    def is_inactive(self):
        return self.status == ReactionStatus.INACTIVE