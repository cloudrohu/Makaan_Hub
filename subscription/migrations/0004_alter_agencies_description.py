# Generated by Django 5.0.2 on 2025-06-27 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0003_alter_follow_up_options_alter_visit_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agencies',
            name='description',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
    ]
