# Generated by Django 5.0.2 on 2025-04-18 05:07

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commercial', '0003_sell_property_parent'),
        ('utility', '0004_alter_amenities_image_alter_bank_image_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Sell_Property',
            new_name='Selly',
        ),
        migrations.RenameModel(
            old_name='Sell_Property_Comment',
            new_name='Selly_Comment',
        ),
        migrations.RenameModel(
            old_name='Sell_Property_Images',
            new_name='Selly_Images',
        ),
    ]
