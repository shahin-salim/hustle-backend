# Generated by Django 4.0.4 on 2022-05-18 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seller', '0005_remove_sellerprofile_education_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sellerprofile',
            name='discription',
            field=models.TextField(),
        ),
    ]
