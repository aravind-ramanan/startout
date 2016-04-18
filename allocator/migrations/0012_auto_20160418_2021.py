# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('allocator', '0011_auto_20160418_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_of_birth', models.DateTimeField(default=datetime.datetime(2016, 4, 18, 20, 21, 0, 884962, tzinfo=utc))),
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
        migrations.RemoveField(
            model_name='userdetails',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserDetails',
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2016, 4, 18, 20, 21, 0, 880905, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
