# Generated by Django 4.1.7 on 2023-05-20 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0026_remove_cartorder_product1_cartorder_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='productt', to='cart.cartitems'),
        ),
    ]