# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-25 18:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('memories', '0005_auto_20170625_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memory',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Lovely Object Name'),
        ),
    ]
