# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-01 13:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shnam_app', '0035_auto_20160801_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='receiver',
            field=models.ForeignKey(default=15, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='shnam_app.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='friend',
            name='sender',
            field=models.ForeignKey(default=15, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='shnam_app.User'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='friend',
            name='receiver_id',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='sender_id',
        ),
        migrations.AlterUniqueTogether(
            name='friend',
            unique_together=set([('sender', 'receiver')]),
        ),
    ]