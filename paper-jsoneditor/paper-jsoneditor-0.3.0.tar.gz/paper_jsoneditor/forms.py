import json

from django import forms

from .widgets import JSONWidget


class JSONField(forms.JSONField):
    empty_values = [None, "", ()]
    widget = JSONWidget

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.show_hidden_initial = False

    def widget_attrs(self, widget):
        attrs = super().widget_attrs(widget)
        attrs["data-options"] = json.dumps(self.get_options())
        attrs["data-ace-options"] = json.dumps(self.get_ace_options())
        return attrs

    def get_options(self):
        """
        JSON-able options for jsoneditor.
        See: https://github.com/josdejong/jsoneditor/blob/develop/docs/api.md#configuration-options
        """
        return {
            "mode": "code",
            "enableSort": False
        }

    def get_ace_options(self):
        """
        JSON-able options for ace.
        See: https://github.com/ajaxorg/ace/wiki/Configuring-Ace
        """
        return {
            "vScrollBarAlwaysVisible": True,
            "fontSize": "18px"
        }
