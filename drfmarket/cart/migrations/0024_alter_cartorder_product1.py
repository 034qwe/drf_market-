# Generated by Django 4.1.7 on 2023-05-19 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0023_alter_cartorder_product1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='product1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cartitems'),
        ),
    ]
