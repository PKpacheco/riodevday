# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-04 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supports', '0002_auto_20161004_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='support',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='support/', verbose_name='Foto'),
        ),
    ]
