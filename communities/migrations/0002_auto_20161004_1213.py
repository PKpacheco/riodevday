# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-04 15:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('communities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='community',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='colaborator/', verbose_name='Foto'),
        ),
        migrations.AlterField(
            model_name='community',
            name='social_network',
            field=models.URLField(blank=True, max_length=255, null=True, verbose_name='Rede Social'),
        ),
    ]
