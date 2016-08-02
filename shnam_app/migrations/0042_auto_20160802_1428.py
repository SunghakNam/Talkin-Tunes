# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-02 14:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shnam_app', '0041_auto_20160802_1426'),
    ]

    operations = [
        migrations.RenameField(
            model_name='friend',
            old_name='receiver',
            new_name='receiverid',
        ),
        migrations.RenameField(
            model_name='friend',
            old_name='sender',
            new_name='senderid',
        ),
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together=set([('senderid', 'receiverid')]),
        ),
    ]
