# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-31 19:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shnam_app', '0029_auto_20160731_1914'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='receiver_id',
            new_name='receiver',
        ),
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together=set([('sender_id', 'receiver')]),
        ),
    ]