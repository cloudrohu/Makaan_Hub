# Generated by Django 5.0.1 on 2024-05-28 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_testimonial_designation_alter_testimonial_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_page',
            name='image',
            field=models.ImageField(upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='contact_page',
            name='image',
            field=models.ImageField(upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='our_team',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='icon',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='logo',
            field=models.ImageField(upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='testmonial_bg',
            field=models.ImageField(upload_to='logo/'),
        ),
        migrations.AlterField(
            model_name='testimonial',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
