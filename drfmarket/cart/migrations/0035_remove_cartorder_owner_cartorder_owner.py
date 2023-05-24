# Generated by Django 4.1.7 on 2023-05-24 18:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0034_remove_cartorder_owner_cartorder_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartorder',
            name='owner',
        ),
        migrations.AddField(
            model_name='cartorder',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='cart.cart'),
            preserve_default=False,
        ),
    ]
