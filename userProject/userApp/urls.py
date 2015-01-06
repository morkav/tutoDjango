# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from userApp import views

urlpatterns = patterns('',
    url(r'^subscribe/$', views.subscribe),
)