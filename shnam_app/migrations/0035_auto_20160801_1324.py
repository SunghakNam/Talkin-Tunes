# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-01 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shnam_app', '0034_auto_20160801_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='receiver_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='sender_id',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
