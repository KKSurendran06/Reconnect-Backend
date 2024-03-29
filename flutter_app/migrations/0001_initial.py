# Generated by Django 5.0.1 on 2024-01-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=20)),
                ('pass_out_year', models.DateField()),
                ('event_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RaiseHand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raisehand', models.BooleanField()),
            ],
        ),
    ]
