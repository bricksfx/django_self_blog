# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_comment_inline'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugTalk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick_name', models.CharField(max_length=200)),
                ('pub_data', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
            ],
            options={
                'verbose_name': '\u5410\u69fdbug',
                'verbose_name_plural': '\u5410\u69fdbug',
            },
            bases=(models.Model,),
        ),
    ]
