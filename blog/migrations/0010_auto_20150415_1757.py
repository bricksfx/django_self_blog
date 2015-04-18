# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_bugtalk'),
    ]

    operations = [
        migrations.CreateModel(
            name='BugTalkInline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nick_name', models.CharField(max_length=200)),
                ('name_pre', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('pub_data', models.DateTimeField(auto_now_add=True)),
                ('bug_pre', models.ForeignKey(to='blog.BugTalk')),
            ],
            options={
                'ordering': ['-pub_data'],
                'verbose_name': '\u5410\u69fdbug\u56de\u590d',
                'verbose_name_plural': '\u5410\u69fdbug\u56de\u590d',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='bugtalk',
            options={'ordering': ['-pub_data'], 'verbose_name': '\u5410\u69fdbug', 'verbose_name_plural': '\u5410\u69fdbug'},
        ),
    ]
