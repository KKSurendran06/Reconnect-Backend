# Generated by Django 5.0.1 on 2024-01-26 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flutter_app', '0003_requestinstitute_delete_requestinsitute_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventpage',
            name='event_time',
            field=models.TimeField(default='12:00'),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='location',
            field=models.CharField(default='Delhi', max_length=25),
        ),
    ]
