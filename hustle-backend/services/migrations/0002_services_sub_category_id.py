# Generated by Django 4.0.4 on 2022-04-21 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subcategory', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='services',
            name='sub_category_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='subcategory.subcategory'),
        ),
    ]
