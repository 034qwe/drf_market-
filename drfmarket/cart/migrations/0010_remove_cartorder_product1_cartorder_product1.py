# Generated by Django 4.1.7 on 2023-05-06 17:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0009_remove_cartorder_product1_cartorder_product1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorder',
            name='product1',
        ),
        migrations.AddField(
            model_name='cartorder',
            name='product1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='cart.cartitems'),
        ),
    ]
