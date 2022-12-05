from django.db import models


def get_default_attribute_schema():
    return {
        'type': 'object',
        'properties': {},
    }


class AttributeSchema(models.Model):
    schema = models.JSONField(default=get_default_attribute_schema)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


def get_latest_attribute_schema_version():
    return AttributeSchema.objects.count()


class AttributeSet(models.Model):
    pseudonym = models.CharField(max_length=128, unique=True)
    attributes = models.JSONField(default=dict)
    attribute_schema = models.ForeignKey(AttributeSchema, on_delete=models.PROTECT,
                                         default=get_latest_attribute_schema_version)
