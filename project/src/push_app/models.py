from django.urls import reverse
from django_extensions.db.fields import AutoSlugField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import TextField
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models
from django_extensions.db import fields as extension_fields


class PushApplication(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    slug = extension_fields.AutoSlugField(populate_from='name', blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=100)
    api_key = models.CharField(max_length=255)

    # Relationship Fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, related_name="pushapplications", 
    )

    class Meta:
        ordering = ('-created',)

    def __unicode__(self):
        return u'%s' % self.slug

    def get_absolute_url(self):
        return reverse('push_app_pushapplication_detail', args=(self.slug,))

    def get_update_url(self):
        return reverse('push_app_pushapplication_update', args=(self.slug,))

    def get_delete_url(self):
        return reverse('push_app_pushapplication_delete', args=(self.slug,))

    def get_tokens(self):
        return reverse('push_app_tokens_list', args=(self.pk,))

    def get_list_push_app(self):
        return reverse('push_app_pushapplication_list')

    def __str__(self):
        return self.name


class RegisteredToken(models.Model):

    token = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    push_app = models.ForeignKey(PushApplication, on_delete=models.CASCADE, related_name='tokens')


class MessageData(models.Model):
    title = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
    token = models.CharField(max_length=255, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    push_app = models.ForeignKey(PushApplication, on_delete=models.CASCADE, related_name='message_datas')


