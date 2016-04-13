# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('allocator', '0003_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 12, 13, 51, 0, 78798, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='project_id',
            field=models.AutoField(serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
