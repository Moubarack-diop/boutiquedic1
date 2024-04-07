from django.urls import path
from . import views

urlpatterns = [
    path("log/", views.view_log, name="log-path"),
]

