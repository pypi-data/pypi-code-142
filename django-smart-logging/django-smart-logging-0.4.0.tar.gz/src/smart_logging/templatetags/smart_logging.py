import json

from django import template

register = template.Library()


@register.filter
def pretty_json(value):
    return json.dumps(value, indent=4, skipkeys=True, default=lambda x: str(x))


@register.filter
def render(value, key):
    return json.dumps(value[key], indent=4, skipkeys=True, default=lambda x: str(x))
