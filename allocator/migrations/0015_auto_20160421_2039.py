# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('allocator', '0014_auto_20160421_0732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 21, 20, 39, 52, 557957, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 21, 20, 39, 52, 560515, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
