from django.core.exceptions import SuspiciousOperation
from djangoldp.views import LDPViewSet, LDPNestedViewSet
from rest_framework.exceptions import ValidationError

from ..models import Annotation
import json

class AnnotationViewset(LDPViewSet):
    def is_safe_create(self, user, validated_data, *args, **kwargs):
        # TODO: check new annotation owner by current user

        target_url_id = validated_data['target']['urlid']
        user_annotation_with_same_target_count = Annotation.objects.filter(creator=user).filter(target__urlid=target_url_id).count()

        if user_annotation_with_same_target_count > 0:
            raise ValidationError({'Attention': ['Vous avez déjà cette ressource dans votre fil.']})
        return True
