# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-16 08:07
from __future__ import unicode_literals

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20170316_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=imagekit.models.fields.ProcessedImageField(blank=True, upload_to='blog/post/%Y/%m/%d'),
        ),
    ]
