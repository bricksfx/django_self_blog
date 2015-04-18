# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
