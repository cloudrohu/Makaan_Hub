# Generated by Django 5.0.1 on 2024-05-28 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercial_project',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='commercial_project_floor_plans',
            name='floor_plan',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='commercial_project_images',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='residential_project',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='residential_project_floor_plans',
            name='floor_plan',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='residential_project_images',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]