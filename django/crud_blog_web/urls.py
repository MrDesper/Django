from django.urls import path
from system_app_app_views import index
urlpatterns = [
    path('test/', index)
]