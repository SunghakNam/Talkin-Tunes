# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-02 15:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shnam_app', '0043_auto_20160802_1429'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('followIdx', models.AutoField(primary_key=True, serialize=False)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('disable', models.BooleanField(default=False)),
                ('followee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followee', to='shnam_app.User')),
                ('follower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower', to='shnam_app.User')),
            ],
        ),
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
        migrations.AddField(
            model_name='musicmsg',
            name='receiver',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='shnam_app.User'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='musicmsg',
            name='sender',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='shnam_app.User'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='musicmsg',
            name='music_receiver',
        ),
        migrations.RemoveField(
            model_name='musicmsg',
            name='music_sender',
        ),
        migrations.AlterUniqueTogether(
            name='musicmsg',
            unique_together=set([('sender', 'receiver')]),
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
        migrations.AlterUniqueTogether(
            name='follow',
            unique_together=set([('follower', 'followee')]),
        ),
    ]
