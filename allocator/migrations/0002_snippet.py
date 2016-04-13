# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('allocator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(default=b'', max_length=100, blank=True)),
                ('code', models.TextField()),
                ('linenos', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('created',),
            },
            bases=(models.Model,),
        ),
    ]
