# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-02 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shnam_app', '0039_auto_20160802_1355'),
    ]

    operations = [
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('playlistIdx', models.AutoField(primary_key=True, serialize=False)),
                ('uri', models.CharField(blank=True, max_length=100, null=True)),
                ('createdTime', models.DateTimeField(auto_now_add=True)),
                ('disable', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to='shnam_app.User')),
            ],
        ),
    ]