# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-01 13:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shnam_app', '0033_auto_20160801_1318'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='friend',
            name='receiver',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='sender',
        ),
    ]
