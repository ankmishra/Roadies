# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-02 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='sender_name',
            field=models.CharField(default=1, max_length=150),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chat',
            name='time',
            field=models.TimeField(null=True),
        ),
    ]
