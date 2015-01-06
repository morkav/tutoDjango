# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response
from userApp.models import Viewer
from userApp.forms import ViewerForm

def subscribe(request):
    if request.method == 'POST':
        pass
    else:
        formset = ViewerForm()
    return render_to_response('userApp/subscribe.html', {'formset':formset})