import logging

from django import forms
from django.conf import settings

from . import conf
from .manager import manager


def _get_handlers():
    if conf.SMART_LOG_HANDLERS:
        for x in manager.handlers.names:
            if x != conf.ONLINE_LOGGER_NAME:
                yield x, x


class FilterLogForm(forms.Form):
    logger = forms.CharField(
        label="",
        required=False,
        widget=forms.TextInput(
            attrs={"placeholder": "Filter by logger name", "class": "search"}
        ),
    )
    level = forms.ChoiceField(label="", required=False, choices=[])

    @property
    def media(self):
        extra = "" if settings.DEBUG else ".min"
        js = ["smart_logging/online%s.js" % extra]
        return forms.Media(js=js)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["level"].choices = (["", "Level"],) + tuple(
            logging._levelToName.items()
        )


class ConfigForm(FilterLogForm):
    handler = forms.ChoiceField(label="", required=False, choices=[])
    propagate = forms.ChoiceField(
        label="",
        required=False,
        choices=[
            ("", "Propagate"),
            ("-1", "Propagate to parent"),
            ("0", "Do not propagate"),
        ],
    )

    @property
    def media(self):
        extra = "" if settings.DEBUG else ".min"
        js = ["smart_logging/config%s.js" % extra]
        return forms.Media(js=js)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if conf.SMART_LOG_HANDLERS > 0:
            handlers = _get_handlers()
            self.fields["handler"].choices = (
                ["", "Handler"],
                ["0", "Any Handler"],
            ) + tuple(handlers)
        else:
            self.fields["handler"].widget = forms.HiddenInput()


class LabelWidget(forms.CheckboxSelectMultiple):
    allow_multiple_selected = True
    input_type = "hidden"


class LoggerConfigForm(forms.Form):
    logger = forms.CharField(max_length=1000, disabled=True, widget=forms.HiddenInput)
    handlers = forms.MultipleChoiceField(
        choices=(), required=False, widget=forms.CheckboxSelectMultiple
    )
    level = forms.TypedChoiceField(choices=logging._levelToName.items(), coerce=int)
    propagate = forms.BooleanField(required=False)
    inspect = forms.BooleanField(required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if conf.SMART_LOG_HANDLERS == conf.HANDLERS_VIEW:
            self.fields["handlers"].widget = LabelWidget()
        self.fields["handlers"].choices = _get_handlers()

    def save(self):
        if self.changed_data:
            logger = logging.getLogger(self.cleaned_data["logger"])
            manager.configure_logger(logger, **self.cleaned_data)
            return self.changed_data
        return []


class LoggerConfigFormSet(forms.BaseFormSet):
    def save(self):
        return {form.cleaned_data["logger"]: form.save() for form in self.forms}


LoggerConfigFormSet = forms.formset_factory(
    LoggerConfigForm, formset=LoggerConfigFormSet, extra=0
)
