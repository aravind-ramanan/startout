# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('allocator', '0010_auto_20160417_0731'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateTimeField(default=datetime.datetime(2016, 4, 18, 18, 36, 24, 101831, tzinfo=utc))),
                ('skills', models.CharField(default='', max_length=100)),
                ('edu_background', models.CharField(default='', max_length=100)),
                ('interests', models.CharField(default='', max_length=100)),
                ('votes', models.IntegerField(default=0)),
                ('profile_pic_loc', models.CharField(default='', max_length=100)),
                ('participated_pid', models.CharField(default='', max_length=200)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='project',
            name='project_manager',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='project',
            name='project_participants',
            field=models.CharField(default='', max_length=100),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 18, 18, 36, 24, 97773, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
