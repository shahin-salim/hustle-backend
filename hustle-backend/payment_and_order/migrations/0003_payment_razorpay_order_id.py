# Generated by Django 4.0.4 on 2022-05-14 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment_and_order', '0002_remove_order_seller_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='razorpay_order_id',
            field=models.CharField(default='1', max_length=230),
        ),
    ]