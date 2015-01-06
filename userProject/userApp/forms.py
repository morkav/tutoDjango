# -*- coding: utf-8 -*-

from django.forms import ModelForm
from userApp.models import Viewer
from django.contrib.auth.models import User

class ViewerForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        # widgets = {
        #     'username' : Textarea,
        # }