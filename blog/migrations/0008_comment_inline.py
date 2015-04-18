# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_comment_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_inline',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('pre_name', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('comment_pre', models.ForeignKey(to='blog.Comment')),
            ],
            options={
                'verbose_name': '\u591a\u7ea7\u8bc4\u8bba',
                'verbose_name_plural': '\u591a\u7ea7\u8bc4\u8bba',
            },
            bases=(models.Model,),
        ),
    ]
