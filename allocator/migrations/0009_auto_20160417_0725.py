# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('allocator', '0008_auto_20160414_1811'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 17, 7, 25, 12, 952, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='edu_background',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='interests',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='participated_pid',
            field=models.CharField(default='', max_length=200),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='profile_pic_loc',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='skills',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='votes',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 17, 7, 25, 11, 999987, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
