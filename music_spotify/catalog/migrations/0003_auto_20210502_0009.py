# Generated by Django 3.1.7 on 2021-05-01 21:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20210502_0005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'permissions': (('can_append_songs', 'can_manage_collection'),)},
        ),
        migrations.AlterField(
            model_name='songinstance',
            name='bought',
            field=models.DateField(default=datetime.datetime(2021, 5, 1, 21, 9, 11, 228157, tzinfo=utc)),
        ),
    ]
