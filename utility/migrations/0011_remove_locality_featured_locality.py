# Generated by Django 5.0.2 on 2025-06-30 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0010_p_amenities'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='locality',
            name='featured_locality',
        ),
    ]
