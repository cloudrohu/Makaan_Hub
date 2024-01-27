# Generated by Django 5.0.1 on 2024-01-27 07:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0002_remove_commercial_project_floor_plans_bed_room'),
        ('utility', '0008_social_site_alter_age_of_properties_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='commercial_project_floor_plans',
            name='floor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='utility.floor'),
        ),
    ]
