from rest_framework import serializers

from huscy.attributes.services import get_or_create_attribute_set
from huscy.data_protection.models import DataAccessRequest, DataRevocationRequest
from huscy.subjects.models import Subject
from huscy.subjects.serializers import SubjectSerializer


class DataAccessRequestSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    creator_name = serializers.CharField(source='creator.get_full_name', read_only=True)

    class Meta:
        model = DataAccessRequest
        fields = 'contact', 'created_at', 'creator', 'creator_name', 'id'
        read_only_fields = 'created_at',


class DataAccessSerializer(serializers.Serializer):
    attributes = serializers.SerializerMethodField()
    subject = serializers.SerializerMethodField()

    def get_attributes(self, contact):
        subject = Subject.objects.get(contact=contact)
        attribute_set = get_or_create_attribute_set(subject)
        return attribute_set.attributes

    def get_subject(self, contact):
        subject = Subject.objects.get(contact=contact)
        return SubjectSerializer(subject).data


class DataRevocationRequestSerializer(serializers.ModelSerializer):
    creator = serializers.HiddenField(default=serializers.CurrentUserDefault())
    creator_name = serializers.CharField(source='creator.get_full_name', read_only=True)

    class Meta:
        model = DataRevocationRequest
        fields = 'contact', 'created_at', 'creator', 'creator_name', 'id', 'type'
        read_only_fields = 'created_at',
