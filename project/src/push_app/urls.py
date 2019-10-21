from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'pushapplication', api.PushApplicationViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for PushApplication
    path('push_app/pushapplication/', views.PushApplicationListView.as_view(), name='push_app_pushapplication_list'),
    path('push_app/pushapplication/create/', views.PushApplicationCreateView.as_view(), name='push_app_pushapplication_create'),
    path('push_app/pushapplication/detail/<slug:slug>/', views.PushApplicationDetailView.as_view(), name='push_app_pushapplication_detail'),
    path('push_app/pushapplication/update/<slug:slug>/', views.PushApplicationUpdateView.as_view(), name='push_app_pushapplication_update'),
    path('push_app/pushapplication/delete/<slug:slug>/', views.PushApplicationDeleteView.as_view(), name='push_app_pushapplication_delete'),
    path('push_app/pushapplication/create_message/', views.CreateMessageView.as_view(), name='push_app_pushapplication_create_message'),
)

