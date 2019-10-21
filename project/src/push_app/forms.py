
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, HTML, Field
from authtools import forms as authtoolsforms
from django.contrib.auth import forms as authforms
from django.urls import reverse

from .models import PushApplication


class PushApplicationForm(forms.ModelForm):
    class Meta:
        model = PushApplication
        fields = ['name', 'description', 'api_key',]


class CreateMessageForm(forms.Form):
    title = forms.CharField(label='Judul')
    message = forms.CharField(label='Pesan')
    token = forms.CharField(label='Token')
    push_app = forms.ModelChoiceField(label='Application', queryset=PushApplication.objects.all())

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'initial' in kwargs:
            if 'user' in kwargs['initial']:
                user = kwargs['initial']['user']
                self.fields['push_app'].queryset = PushApplication.objects.filter(user=kwargs['initial']['user'])

