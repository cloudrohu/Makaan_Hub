# Generated by Django 5.0.2 on 2025-04-17 07:35

import django.db.models.deletion
import mptt.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0002_alter_sell_property_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell_property',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='commercial.sell_property'),
        ),
    ]
