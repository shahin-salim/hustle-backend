# Generated by Django 4.0.4 on 2022-04-21 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_services_sub_category_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Services',
        ),
    ]
