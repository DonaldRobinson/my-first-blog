# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 23:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180416_1803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
    ]
