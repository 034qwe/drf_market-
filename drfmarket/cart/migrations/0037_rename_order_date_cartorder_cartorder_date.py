# Generated by Django 4.1.7 on 2023-05-26 19:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0036_rename_cartorder_date_cartorder_order_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartorder',
            old_name='order_date',
            new_name='cartorder_date',
        ),
    ]
