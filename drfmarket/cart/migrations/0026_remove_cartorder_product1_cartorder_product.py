# Generated by Django 4.1.7 on 2023-05-20 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0025_alter_cartorder_product1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorder',
            name='product1',
        ),
        migrations.AddField(
            model_name='cartorder',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cartitems'),
        ),
    ]