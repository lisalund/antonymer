# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-31 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('antonymapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WordPair',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word1', models.TextField()),
                ('word2', models.TextField()),
                ('ones', models.IntegerField(default=0)),
                ('two', models.IntegerField(default=0)),
                ('three', models.IntegerField(default=0)),
                ('four', models.IntegerField(default=0)),
                ('five', models.IntegerField(default=0)),
            ],
        ),
    ]
