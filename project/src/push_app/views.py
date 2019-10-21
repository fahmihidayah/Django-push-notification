from django.views.generic import DetailView, ListView, UpdateView, CreateView, DeleteView, TemplateView
from .models import PushApplication
from .forms import PushApplicationForm, CreateMessageForm

from django.urls import reverse_lazy

from django.shortcuts import redirect

from django.contrib import messages
from .tables import PushApplicationTable
from django.contrib.auth.mixins import LoginRequiredMixin
import django_tables2

from pyfcm import FCMNotification

class PushApplicationListView(LoginRequiredMixin,  django_tables2.SingleTableView):
    model = PushApplication
    paginate_by = 10
    table_class = PushApplicationTable

    def get_queryset(self):
        return PushApplication.objects.filter(user=self.request.user)


class PushApplicationCreateView(LoginRequiredMixin, CreateView):
    model = PushApplication
    form_class = PushApplicationForm

    def form_valid(self, form):
        data: PushApplication = form.save(commit=False)
        data.user = self.request.user
        return super(PushApplicationCreateView, self).form_valid(form)

    def get_success_url(self):
        messages.success(
            self.request,
            "Data successful created", )
        return reverse_lazy('push_app_pushapplication_list')

class PushApplicationDetailView(LoginRequiredMixin, DetailView):
    model = PushApplication


class PushApplicationUpdateView(LoginRequiredMixin, UpdateView):
    model = PushApplication
    form_class = PushApplicationForm

    def get_success_url(self):
        messages.success(
            self.request,
            "Data successful created", )
        return reverse_lazy('push_app_pushapplication_list')


class PushApplicationDeleteView(LoginRequiredMixin, DeleteView):
    model = PushApplication

    def get_success_url(self):
        messages.success(
            self.request,
            "Data successful deleted",)
        return reverse_lazy('push_app_pushapplication_list')


class CreateMessageView(LoginRequiredMixin, TemplateView):
    http_method_names = ['post', 'get']
    template_name = "push_app/pushapplication_message_form.html"

    def get_context_data(self, **kwargs):
        context = super(CreateMessageView, self).get_context_data(**kwargs)
        print(self.request.user)
        context['form'] = CreateMessageForm(initial={'user':self.request.user})
        return context


    def post(self, request, *args, **kwargs):
        form : CreateMessageForm = CreateMessageForm(request.POST)
        is_valid = form.is_valid()
        push_app : PushApplication = form.cleaned_data['push_app']

        push_service : FCMNotification = FCMNotification(api_key=push_app.api_key)

        result = push_service.notify_single_device(registration_id=form.cleaned_data['token'],
                                          message_title=form.cleaned_data['title'],
                                          message_body=form.cleaned_data['message'])
        messages.success(
            self.request,
            result, )

        return redirect('push_app_pushapplication_create_message')





