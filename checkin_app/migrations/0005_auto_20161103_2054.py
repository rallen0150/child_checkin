# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-03 20:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin_app', '0004_auto_20161103_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='child',
            name='pin_number',
            field=models.CharField(max_length=4, unique=True),
        ),
    ]
