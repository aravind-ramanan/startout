# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('allocator', '0005_auto_20160414_0458'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_owner',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 14, 18, 10, 41, 879461, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
