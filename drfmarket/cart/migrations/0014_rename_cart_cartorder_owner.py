# Generated by Django 4.1.7 on 2023-05-07 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0013_alter_cartorder_product1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartorder',
            old_name='cart',
            new_name='owner',
        ),
    ]
