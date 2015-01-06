# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


# On peut également mapper une URL à une vue en passant directement la vue
# importée (et nom une chaîne, comme dans app1)
from app1_hello.views import hello
from app2_hello_again.views import plap


urlpatterns = patterns('',
    url(r'plap', plap, name='include'),
    url(r'', hello),
)
