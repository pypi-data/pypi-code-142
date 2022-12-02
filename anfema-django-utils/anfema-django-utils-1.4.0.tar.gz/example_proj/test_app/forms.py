from django import forms

from .models import DenyFieldUpdateTriggerTestModel


class DenyFieldUpdateTriggerModelForm(forms.ModelForm):
    class Meta:
        model = DenyFieldUpdateTriggerTestModel
        fields = '__all__'
