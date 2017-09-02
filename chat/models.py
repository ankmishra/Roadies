# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Chat(models.Model):
    sender = models.ForeignKey(User)
    message = models.CharField(max_length=1500)
    reciever = models.CharField(max_length=150)
    reciever = models.CharField(max_length=150)
    sender_name = models.CharField(max_length=150)
    time = models.TimeField(null=True)
