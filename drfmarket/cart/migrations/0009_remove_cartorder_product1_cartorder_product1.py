# Generated by Django 4.1.7 on 2023-05-06 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0008_alter_cartorder_product1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorder',
            name='product1',
        ),
        migrations.AddField(
            model_name='cartorder',
            name='product1',
            field=models.ManyToManyField(blank=True, null=True, related_name='item', to='cart.cartitems'),
        ),
    ]
