# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20150410_2216'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
