# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-08 12:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_tweet_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='reply',
            field=models.BooleanField(default=False, verbose_name='Is a reply?'),
        ),
    ]
