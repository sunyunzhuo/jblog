# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-13 03:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20170412_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='timestamp',
            field=models.DateField(default=datetime.datetime(2017, 4, 13, 11, 16, 19, 33000)),
        ),
    ]
