import django_tables2 as tables
from .models import PushApplication, RegisteredToken, MessageData

class PushApplicationTable(tables.Table):
    edit = tables.TemplateColumn(template_name='table/edit.html')

    delete = tables.TemplateColumn(template_name='table/delete.html')

    detail = tables.TemplateColumn(template_name='table/detail.html')

    list_token = tables.TemplateColumn(template_name='push_app/table/list_token.html')

    class Meta:
        model = PushApplication
        fields = ['id', 'name', 'description', 'created', 'last_updated']
        template_name = 'django_tables2/bootstrap.html'


class RegisteredTokenTable(tables.Table):

    class Meta:
        model = RegisteredToken
        fields = ['id', 'token', 'created', 'last_updated']
        template_name = 'django_tables2/bootstrap.html'


class MessageDataTable(tables.Table):

    detail = tables.TemplateColumn(template_name='table/detail.html')
    action = tables.TemplateColumn(template_name='push_app/table/resend.html')

    class Meta:
        model = MessageData
        fields = ['id', 'title', 'message', 'is_single']
        template_name = 'django_tables2/bootstrap.html'