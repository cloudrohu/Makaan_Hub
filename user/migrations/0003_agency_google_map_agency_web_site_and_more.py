# Generated by Django 5.0.1 on 2024-01-27 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_agency_find_from_developer_find_from'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='google_map',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='agency',
            name='web_site',
            field=models.CharField(blank=True, max_length=150),
        ),
        migrations.AddField(
            model_name='developer',
            name='google_map',
            field=models.CharField(blank=True, max_length=1000),
        ),
        migrations.AddField(
            model_name='developer',
            name='web_site',
            field=models.CharField(blank=True, max_length=150),
        ),
    ]
