# Generated by Django 5.0.1 on 2024-01-27 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commercial_project_floor_plans',
            name='bed_room',
        ),
    ]
