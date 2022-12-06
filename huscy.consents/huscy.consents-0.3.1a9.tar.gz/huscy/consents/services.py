from django.apps import apps

from huscy.consents.models import TextFragment


def create_text_fragment(consent, element_type, element_data):
    element = create_element(element_type, **element_data)
    order = TextFragment.objects.filter(consent=consent).count()
    return TextFragment.objects.create(consent=consent, element=element, order=order)


def create_element(element_type, **element_data):
    assert element_type in 'Checkbox Header Paragraph'.split(), 'unsupported element type'

    Element = apps.get_model('consents', element_type)
    return Element.objects.create(**element_data)
