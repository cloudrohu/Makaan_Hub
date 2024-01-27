# Generated by Django 5.0.1 on 2024-01-27 04:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_rename_fax_setting_whatsapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('comment', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/')),
                ('status', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
            ],
        ),
    ]
