# Generated by Django 3.0.3 on 2020-02-07 01:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('absence', '0002_auto_20200207_0211'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotion',
            name='annee',
            field=models.DateTimeField(default=datetime.datetime(2020, 2, 7, 1, 21, 47, 776446, tzinfo=utc)),
        ),
    ]
