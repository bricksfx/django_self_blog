# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20150415_1757'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=20)),
                ('body', django_markdown.models.MarkdownField()),
            ],
            options={
                'verbose_name': '\u5173\u4e8e\u6211\u4eec',
                'verbose_name_plural': '\u5173\u4e8e\u6211\u4eec',
            },
            bases=(models.Model,),
        ),
        migrations.AlterModelOptions(
            name='bugtalk',
            options={'verbose_name': '\u5410\u69fdbug', 'verbose_name_plural': '\u5410\u69fdbug'},
        ),
    ]
