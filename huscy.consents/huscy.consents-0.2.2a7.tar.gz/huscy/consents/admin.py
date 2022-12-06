from django.contrib import admin
from django.template.defaultfilters import truncatechars

from huscy.consents import models


class ConsentAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name'


class ConsentCategoryAdmin(admin.ModelAdmin):
    list_display = 'pk', 'name'


class ConsentFileAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = 'consent', 'created_at', 'filehandle'
    readonly_fields = 'created_at',


class TextFragmentAdmin(admin.ModelAdmin):
    list_display = 'consent', '_element', '_text', 'order'

    def _element(self, text_fragment):
        return text_fragment.element.__class__.__name__

    def _text(self, text_fragment):
        return truncatechars(text_fragment.element.text, 120)


admin.site.register(models.Checkbox)
admin.site.register(models.Consent, ConsentAdmin)
admin.site.register(models.ConsentCategory, ConsentCategoryAdmin)
admin.site.register(models.ConsentFile, ConsentFileAdmin)
admin.site.register(models.Paragraph)
admin.site.register(models.TemplateTextFragment)
admin.site.register(models.TextFragment, TextFragmentAdmin)
