# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-15 07:30
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=True)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.Article')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='comment',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 15, 7, 30, 3, 639892, tzinfo=utc), verbose_name='Date Published'),
            preserve_default=False,
        ),
    ]
