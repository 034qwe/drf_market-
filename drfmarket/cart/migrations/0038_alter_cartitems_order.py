# Generated by Django 4.1.7 on 2023-05-26 19:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0037_rename_order_date_cartorder_cartorder_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitems',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cartorder'),
        ),
    ]
