# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-16 17:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinformation', '0002_remove_userinformations_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformations',
            name='access_key',
            field=models.CharField(max_length=240, null=True),
        ),
    ]
