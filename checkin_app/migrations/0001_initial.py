# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-06 01:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Child',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=25)),
                ('pincode', models.CharField(max_length=4, unique=True)),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_level', models.CharField(choices=[('P', 'Parent'), ('E', 'Employee')], max_length=1)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Time',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.BooleanField(default=False)),
                ('checkin_time', models.DateTimeField(auto_now_add=True)),
                ('checkout_time', models.DateTimeField(null=True)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkin_app.Child')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
