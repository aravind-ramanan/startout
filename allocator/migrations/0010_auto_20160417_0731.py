# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('allocator', '0009_auto_20160417_0725'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='edu_background',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='interests',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='participated_pid',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_pic_loc',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='votes',
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 17, 7, 31, 11, 307846, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
