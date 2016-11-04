# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-04 18:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('checkin_app', '0002_auto_20161104_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin_time', models.DateTimeField()),
                ('checkout_time', models.DateTimeField()),
            ],
        ),
        migrations.RemoveField(
            model_name='child',
            name='checkin_time',
        ),
        migrations.RemoveField(
            model_name='child',
            name='checkout_time',
        ),
        migrations.AddField(
            model_name='time',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkin_app.Child'),
        ),
    ]