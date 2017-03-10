#from django.conf.urls import patterns, url 
from django_app import views
from django.conf.urls import * 
from django.contrib import admin 
admin.autodiscover()
urlpatterns = [
url(r'^$', views.index)
]