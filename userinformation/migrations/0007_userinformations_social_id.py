# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-10 18:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinformation', '0006_remove_userinformations_social_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinformations',
            name='social_id',
            field=models.CharField(max_length=120, null=True),
        ),
    ]