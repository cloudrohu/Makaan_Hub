# Generated by Django 5.0.2 on 2025-07-30 07:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subscription', '0008_meta_response_created_by_meta_response_updated_by'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='agencies',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created_agencies', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agencies',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_agencies', to=settings.AUTH_USER_MODEL),
        ),
    ]
