# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-02 14:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shnam_app', '0040_playlist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='musicmsg',
            old_name='receiver',
            new_name='music_receiver',
        ),
        migrations.RenameField(
            model_name='musicmsg',
            old_name='sender',
            new_name='music_sender',
        ),
        migrations.AlterUniqueTogether(
            name='musicmsg',
            unique_together=set([('music_sender', 'music_receiver')]),
        ),
    ]