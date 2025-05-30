# Generated by Django 5.0.2 on 2025-04-18 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_alter_commercial_project_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commercial_project',
            name='propert_type',
            field=models.CharField(choices=[('Ready to move offices', 'Ready to move offices'), ('Shops & Retail', 'Shops & Retail'), ('Agricultural/Farm Land', 'Agricultural/Farm Land'), ('Industrial Land/Plots', 'Industrial Land/Plots'), ('Warehouse', 'Warehouse'), ('Factory & Manufacturing', 'Factory & Manufacturing'), ('Bare shell offices', 'Bare shell offices'), ('Commercial/Inst. Land', 'Commercial/Inst. Land'), ('Cold Storage', 'Cold Storage'), ('Hotel/Resorts', 'Hotel/Resorts')], default=2, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='residential_project',
            name='propert_type',
            field=models.CharField(choices=[('1 RK Studio Apartment', '1 RK Studio Apartment'), ('Agricultural Farm Land', 'Agricultural Farm Land'), ('Farm House', 'Farm House'), ('Independent Builder Floor', 'Independent House Villa'), ('Residential Apartment', 'Residential Apartment')], max_length=200),
        ),
    ]
