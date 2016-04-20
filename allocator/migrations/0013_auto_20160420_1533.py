# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import re
from django.utils.timezone import utc
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('allocator', '0012_auto_20160418_2021'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='requests',
            field=models.CharField(default='0', max_length=100, validators=[django.core.validators.RegexValidator(re.compile('^[\\d,]+$'), 'Enter only digits separated by commas.', 'invalid')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 20, 15, 33, 37, 747631, tzinfo=utc)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='project_participants',
            field=models.CharField(default='0', max_length=100, validators=[django.core.validators.RegexValidator(re.compile('^[\\d,]+$'), 'Enter only digits separated by commas.', 'invalid')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userdetail',
            name='date_of_birth',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 20, 15, 33, 37, 750122, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
