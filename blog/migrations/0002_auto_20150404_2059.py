# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_markdown.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='article',
            name='body',
            field=django_markdown.models.MarkdownField(),
        ),
    ]
