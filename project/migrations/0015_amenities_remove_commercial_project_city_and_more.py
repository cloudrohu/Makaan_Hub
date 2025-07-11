# Generated by Django 5.0.2 on 2025-06-29 15:57

import django.db.models.deletion
import mptt.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0014_alter_residential_project_total_floor'),
        ('user', '0008_alter_agency_image_alter_developer_image'),
        ('utility', '0009_remove_locality_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('icon', models.ImageField(blank=True, null=True, upload_to='amenities/')),
            ],
        ),
        migrations.RemoveField(
            model_name='commercial_project',
            name='city',
        ),
        migrations.RemoveField(
            model_name='commercial_project',
            name='developer',
        ),
        migrations.RemoveField(
            model_name='commercial_project',
            name='home_lone',
        ),
        migrations.RemoveField(
            model_name='commercial_project',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='commercial_project',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='commercial_project_floor_plans',
            name='commercial_project',
        ),
        migrations.RemoveField(
            model_name='commercial_project_comment',
            name='project',
        ),
        migrations.RemoveField(
            model_name='commercial_project_comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='residential_project',
            name='city',
        ),
        migrations.RemoveField(
            model_name='residential_project',
            name='developer',
        ),
        migrations.RemoveField(
            model_name='residential_project',
            name='home_lone',
        ),
        migrations.RemoveField(
            model_name='residential_project',
            name='locality',
        ),
        migrations.RemoveField(
            model_name='residential_project',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='residential_project_floor_plans',
            name='Project',
        ),
        migrations.RemoveField(
            model_name='residential_project_images',
            name='project',
        ),
        migrations.RemoveField(
            model_name='residential_project_comment',
            name='project',
        ),
        migrations.RemoveField(
            model_name='residential_project_comment',
            name='user',
        ),
        migrations.CreateModel(
            name='Residential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('construction_status', models.CharField(choices=[('Under Construction', 'Under Construction'), ('New Launch', 'New Launch'), ('Partially Ready To Move', 'Partially Ready To Move'), ('Ready To Move', 'Ready To Move'), ('Deleverd', 'Deleverd')], max_length=25)),
                ('propert_type', models.CharField(choices=[('1 RK Studio Apartment', '1 RK Studio Apartment'), ('Agricultural Farm Land', 'Agricultural Farm Land'), ('Farm House', 'Farm House'), ('Independent Builder Floor', 'Independent House Villa'), ('Residential Apartment', 'Residential Apartment')], max_length=200)),
                ('project_name', models.CharField(max_length=250)),
                ('Possession', models.CharField(max_length=50)),
                ('land_parceland', models.CharField(max_length=50)),
                ('floor', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=150, null=True)),
                ('price', models.TextField(blank=True, max_length=150, null=True)),
                ('keywords', models.CharField(max_length=255)),
                ('meta_description', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='images/')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.city')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.developer')),
                ('locality', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='utility.locality')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='project.residential')),
            ],
            options={
                'verbose_name_plural': '1. Residential Project',
            },
        ),
        migrations.CreateModel(
            name='RERAAdditional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rera_extra', to='project.residential')),
            ],
        ),
        migrations.CreateModel(
            name='Project_Amenities',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='project.amenities')),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='amenities', to='project.residential')),
            ],
        ),
        migrations.CreateModel(
            name='Overview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='overviews', to='project.residential')),
            ],
        ),
        migrations.CreateModel(
            name='MahaRERA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_no', models.CharField(max_length=100)),
                ('document', models.FileField(upload_to='rera_docs/')),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rera', to='project.residential')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255)),
                ('google_map_iframe', models.TextField(blank=True)),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='project.residential')),
            ],
        ),
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('subtitle', models.CharField(blank=True, max_length=255)),
                ('background_image', models.ImageField(upload_to='headers/')),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='headers', to='project.residential')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery/')),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gallery', to='project.residential')),
            ],
        ),
        migrations.CreateModel(
            name='Configuration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bhk_type', models.CharField(max_length=50)),
                ('area', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=100)),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='configs', to='project.residential')),
            ],
        ),
        migrations.CreateModel(
            name='BookingOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='BookingOffer', to='project.residential')),
            ],
        ),
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='aboutus', to='project.residential')),
            ],
        ),
        migrations.CreateModel(
            name='USP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.CharField(max_length=255)),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='usps', to='project.residential')),
            ],
        ),
        migrations.CreateModel(
            name='WebSlider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='web_slider/')),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sliders', to='project.residential')),
            ],
        ),
        migrations.CreateModel(
            name='WelcomeTo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='welcomes', to='project.residential')),
            ],
        ),
        migrations.CreateModel(
            name='WhyInvest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.TextField()),
                ('residential', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='why_invest', to='project.residential')),
            ],
        ),
        migrations.DeleteModel(
            name='Commercial_Project_Images',
        ),
        migrations.DeleteModel(
            name='Commercial_Project_Floor_Plans',
        ),
        migrations.DeleteModel(
            name='Commercial_Project',
        ),
        migrations.DeleteModel(
            name='Commercial_Project_Comment',
        ),
        migrations.DeleteModel(
            name='Residential_Project_Floor_Plans',
        ),
        migrations.DeleteModel(
            name='Residential_Project_Images',
        ),
        migrations.DeleteModel(
            name='Residential_Project',
        ),
        migrations.DeleteModel(
            name='Residential_Project_Comment',
        ),
    ]
