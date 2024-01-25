# Generated by Django 5.0.1 on 2024-01-25 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flutter_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EditProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageurl', models.CharField(max_length=20)),
                ('aboutus', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='InstituteDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=20)),
                ('graduationyear', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='RequestInsitute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requestInsituteName', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='description',
            field=models.CharField(max_length=250),
        ),
    ]
