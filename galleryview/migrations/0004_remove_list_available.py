# Generated by Django 3.1.2 on 2020-11-30 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galleryview', '0003_list_available'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list',
            name='available',
        ),
    ]
