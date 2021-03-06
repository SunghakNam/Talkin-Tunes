# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-31 19:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shnam_app', '0028_auto_20160731_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='receiver',
            new_name='receiver_id',
        ),
        migrations.RenameField(
            model_name='friend',
            old_name='sender',
            new_name='sender_id',
        ),
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together=set([('sender_id', 'receiver_id')]),
        ),
    ]
