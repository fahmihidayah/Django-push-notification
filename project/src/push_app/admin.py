from django.contrib import admin
from django import forms
from .models import PushApplication

class PushApplicationAdminForm(forms.ModelForm):

    class Meta:
        model = PushApplication
        fields = '__all__'


class PushApplicationAdmin(admin.ModelAdmin):
    form = PushApplicationAdminForm
    list_display = ['name', 'slug', 'created', 'last_updated', 'description', 'api_key']
    readonly_fields = ['name', 'slug', 'created', 'last_updated', 'description', 'api_key']

admin.site.register(PushApplication, PushApplicationAdmin)


