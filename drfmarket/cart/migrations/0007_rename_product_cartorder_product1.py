# Generated by Django 4.1.7 on 2023-05-06 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0006_cartorder_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartorder',
            old_name='product',
            new_name='product1',
        ),
    ]
