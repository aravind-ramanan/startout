# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('allocator', '0002_snippet'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_name', models.CharField(max_length=30)),
                ('project_id', models.IntegerField(serialize=False, primary_key=True)),
                ('project_logo', models.CharField(max_length=100)),
                ('date_created', models.DateTimeField(default=datetime.datetime(2016, 4, 11, 3, 24, 45, 407620, tzinfo=utc))),
                ('description', models.CharField(max_length=50)),
                ('category', models.CharField(max_length=30)),
                ('skills_reqd', models.CharField(max_length=100)),
                ('edu_background_reqd', models.CharField(max_length=100)),
                ('payment', models.IntegerField(default=0)),
                ('status', models.CharField(max_length=15)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
