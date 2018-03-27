# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-27 20:50
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crawlr', '0003_auto_20180327_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='liked_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
