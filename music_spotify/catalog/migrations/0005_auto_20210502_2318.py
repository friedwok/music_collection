# Generated by Django 3.2 on 2021-05-02 20:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_auto_20210502_1924'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ['author'], 'permissions': (('can_append_songs', 'can_manage_collection'),)},
        ),
        migrations.AddField(
            model_name='author',
            name='info',
            field=models.TextField(default='No info about this author.', help_text='Enter some info about author', max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='songinstance',
            name='bought',
            field=models.DateField(default=datetime.datetime(2021, 5, 2, 20, 18, 8, 16469, tzinfo=utc)),
        ),
    ]
