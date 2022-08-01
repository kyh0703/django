from importlib.resources import path
from pathlib import Path


from django.urls import path
from . import views

urlpatterns = [path("", views.list_patients, name="list_patients")]
