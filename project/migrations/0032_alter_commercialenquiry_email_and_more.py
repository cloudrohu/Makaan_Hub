# Generated by Django 5.0.2 on 2025-07-06 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0031_commercialproject_commercialoverview_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercialenquiry',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='residentialenquiry',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
