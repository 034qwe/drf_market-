# Generated by Django 4.1.7 on 2023-05-08 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0017_alter_cartorder_product1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartorder',
            name='product1',
            field=models.ManyToManyField(blank=True, to='cart.cartitems'),
        ),
    ]