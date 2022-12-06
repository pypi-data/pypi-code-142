from django.conf import settings
from rest_framework import serializers
from wagtail import blocks
from django.utils.translation import gettext_lazy as _
from wagtail.blocks import StreamBlock

from wagtail_rest_pack.streamfield.serializers import SettingsStreamFieldSerializer

rest_pack = getattr(settings, "REST_PACK", {})
icons = rest_pack.get('icons', [])


class LinkCategorySerializer(serializers.Serializer):
    block_name = 'linkcategory'

    name = serializers.CharField(max_length=50)
    icon = serializers.CharField()
    stream = SettingsStreamFieldSerializer()

    @staticmethod
    def block_definition(local_blocks):
        return LinkCategorySerializer.block_name, blocks.StructBlock(local_blocks=[
            ('name', blocks.TextBlock(max_length=50, required=True, help_text=_('Name of the category'))),
            ('stream', StreamBlock(local_blocks, label=_('A nested content of a category'))),
            ('icon', blocks.ChoiceBlock(choices=[('none', _('None'))] + icons, default=['none'], label=_('The icon'))),
        ])

    class Meta:
        fields = ['name', 'stream', 'icon']


class FacebookLinkSerializer(serializers.Serializer):
    block_name = 'fblink'
    url = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=200)

    @staticmethod
    def block_definition():
        local_block_name = FacebookLinkSerializer.block_name
        return local_block_name, blocks.StructBlock(local_blocks=[
            ('url', blocks.TextBlock(max_length=200, required=True, help_text=_('Celý odkaz na facebook'))),
            ('text', blocks.TextBlock(max_length=200, required=True, help_text=_('Text odkazu'))),
        ])

    class Meta:
        fields = ['url','text']

class EmailLinkSerializer(serializers.Serializer):
    block_name = 'emaillink'
    email = serializers.CharField(max_length=200)

    @staticmethod
    def block_definition():
        local_block_name = EmailLinkSerializer.block_name
        return local_block_name, blocks.StructBlock(local_blocks=[
            ('email', blocks.TextBlock(max_length=200, required=True, help_text=_('Kontaktní email'))),
        ])

    class Meta:
        fields = ['email']

class HeaderSerializer(serializers.Serializer):
    block_name = 'footerheader'
    text = serializers.CharField(max_length=200)
    stream = SettingsStreamFieldSerializer()

    @staticmethod
    def block_definition(local_blocks):
        local_block_name = HeaderSerializer.block_name
        return local_block_name, blocks.StructBlock(local_blocks=[
            ('text', blocks.TextBlock(max_length=200, required=True, help_text=_('Nadpis části'))),
            ('stream', StreamBlock(local_blocks, label=_('Bloky'))),
        ])

    class Meta:
        fields = ['text', 'stream']

class ContactFormLinkSerializer(serializers.Serializer):
    block_name = 'contactform'
    url = serializers.CharField(max_length=200)
    text = serializers.CharField(max_length=200)

    @staticmethod
    def block_definition():
        local_block_name = ContactFormLinkSerializer.block_name
        return local_block_name, blocks.StructBlock(local_blocks=[
            ('url', blocks.TextBlock(max_length=200, required=True, help_text=_('Relativní cesta na kontaktní formulář, např. /contact-us#form'))),
            ('text', blocks.TextBlock(max_length=200, required=True, help_text=_('Text odkazu'))),
        ])

    class Meta:
        fields = ['url','text']


class LinkBlockSerializer(serializers.Serializer):
    block_name = 'linkblock'

    name = serializers.CharField(max_length=50)
    icon = serializers.CharField()
    page = serializers.SerializerMethodField('get_page_repre')

    @staticmethod
    def block_definition(nested:bool=False):
        local_block_name = LinkBlockSerializer.block_name
        if nested:
            local_block_name = 'nested'+local_block_name
        return local_block_name, blocks.StructBlock(local_blocks=[
            ('name', blocks.TextBlock(max_length=50, required=True, help_text=_('Name of the link'))),
            ('page', blocks.PageChooserBlock(label=_('A page to be opened'))),
            ('icon', blocks.ChoiceBlock(choices=[('none', _('None'))] + icons, default=['none'], label=_('The icon'))),
        ])

    def get_page_repre(self, value):
        page = value['page']
        return {
            'id': page.id,
            'url': page.url,
        }

    class Meta:
        fields = ['name', 'page', 'icon']



class ChildrenLinksSerializer(serializers.Serializer):
    block_name = 'categorychildren'
    children = serializers.SerializerMethodField('get_page_repre')

    @staticmethod
    def block_definition():
        return ChildrenLinksSerializer.block_name, blocks.StructBlock(local_blocks=[
            ('parent', blocks.PageChooserBlock(label=_('A page which children should be listed'))),
        ])

    def get_page_repre(self, value):
        parent = value['parent']
        children_qs = parent.specific.children
        # todo limit somehow, or filter according to "show_in_menus"
        children = map(lambda child: {'name': child.title, 'page': child, 'icon':''}, children_qs)
        return LinkBlockSerializer(instance=children, many=True).data

    class Meta:
          fields = ['children',]