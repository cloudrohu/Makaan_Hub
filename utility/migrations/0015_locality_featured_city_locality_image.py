# Generated by Django 5.0.2 on 2025-07-24 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0014_delete_possession_in'),
    ]

    operations = [
        migrations.AddField(
            model_name='locality',
            name='featured_city',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='locality',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
