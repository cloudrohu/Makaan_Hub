# Generated by Django 5.0.2 on 2025-06-30 07:42

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_remove_welcometo_title_welcometo_description_and_more'),
        ('utility', '0011_remove_locality_featured_locality'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingoffer',
            name='bank_approval',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='booking_offers', to='utility.bank'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookingoffer',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='residential',
            name='Commencement_Certificate',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='residential',
            name='Occupancy_Certificate',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='residential',
            name='possession_year',
            field=models.CharField(blank=True, choices=[('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021'), ('2022', '2022'), ('2023', '2023'), ('2024', '2024'), ('2025', '2025'), ('2026', '2026'), ('2027', '2027'), ('2028', '2028'), ('2029', '2029'), ('2030', '2030'), ('2031', '2031'), ('2032', '2032'), ('2033', '2033'), ('2034', '2034'), ('2035', '2035'), ('2036', '2036'), ('2037', '2037'), ('2038', '2038'), ('2039', '2039')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='bookingoffer',
            name='residential',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking_offers', to='project.residential'),
        ),
        migrations.AlterField(
            model_name='bookingoffer',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
