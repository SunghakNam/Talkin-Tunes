# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-02 15:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shnam_app', '0054_auto_20160802_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='musicmsg',
            name='followObj',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='follow_obj', to='shnam_app.Follow'),
            preserve_default=False,
        ),
    ]
