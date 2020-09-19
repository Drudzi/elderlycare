"""Defines URL patterns for elders app."""

from django.urls import path

from . import views

app_name = 'elders'

urlpatterns = [
    # Home page:
    path('', views.home, name='home'),
]