# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2018-02-15 19:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0002_lesson_is_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]