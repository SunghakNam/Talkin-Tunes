# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-31 19:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shnam_app', '0026_auto_20160731_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shnam_app.User'),
        ),
    ]
