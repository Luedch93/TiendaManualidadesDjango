# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-17 14:15
from __future__ import unicode_literals

from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagen',
            field=stdimage.models.StdImageField(blank=True, upload_to='post/%Y/%m/%d'),
        ),
    ]
