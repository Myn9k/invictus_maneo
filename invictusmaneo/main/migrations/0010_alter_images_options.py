# Generated by Django 4.2.4 on 2024-04-06 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_images_remove_files_images'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='images',
            options={'verbose_name': 'Image', 'verbose_name_plural': 'Images'},
        ),
    ]
