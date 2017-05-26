# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-22 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time']},
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='views',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
