# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-03 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_auto_20170501_2127'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='skills',
            field=models.ManyToManyField(blank=True, default=b'', related_name='skills', to='projects.Skill'),
        ),
    ]