# Generated by Django 5.0.1 on 2024-01-26 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_our_team_featured_our_team_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Header',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(blank=True, upload_to='logo/')),
                ('header_footer_color', models.CharField(blank=True, max_length=150)),
                ('title', models.CharField(blank=True, max_length=150)),
            ],
        ),
    ]