# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-11 10:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0008_auto_20180611_0922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='patient_file',
        ),
    ]