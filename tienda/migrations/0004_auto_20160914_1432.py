# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0003_auto_20160914_1430'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, height_field='url_height', upload_to='productos/%d/%m/%Y', width_field='url_width'),
        ),
    ]