# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('allocator', '0015_auto_20160421_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 22, 5, 12, 46, 960765, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 22, 5, 12, 46, 964860, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
