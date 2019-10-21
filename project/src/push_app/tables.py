import django_tables2 as tables
from .models import PushApplication

class PushApplicationTable(tables.Table):
    # edit = tables.TemplateColumn(template_name='table/edit.html')
    #
    # delete = tables.TemplateColumn(template_name='table/delete.html')
    #
    # detail = tables.TemplateColumn(template_name='table/detail.html')
    # #
    # change_status = tables.TemplateColumn(template_name='todos/table/set_done.html')

    class Meta:
        model = PushApplication
        fields = ['id', 'name', 'description', 'api_key', 'last_updated']
        template_name = 'django_tables2/bootstrap.html'