from django.contrib import admin
from django.conf.urls import url
from django.views.generic import TemplateView
# from django.urls import path

from . import views

app_name = "sendemails"
urlpatterns = [
    url(r'^$', views.emailView, name='email'),
    url(r'^$', views.successView, name='success'),
    # url(r'^/', emailView.as_view(), name='email'),
    # url(r'^/success/', successView.as_view(), name='success'),
]