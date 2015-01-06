# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User

class Viewer(models.Model):
    """
        Test for inscription of users
    """
    user = models.OneToOneField(User)

    def __unicode__(self):
        return u'{0}'.format(self.user.username)
