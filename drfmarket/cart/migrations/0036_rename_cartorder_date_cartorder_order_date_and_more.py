# Generated by Django 4.1.7 on 2023-05-26 18:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cart', '0035_remove_cartorder_owner_cartorder_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartorder',
            old_name='cartorder_date',
            new_name='order_date',
        ),
        migrations.RemoveField(
            model_name='cartorder',
            name='product',
        ),
        migrations.AddField(
            model_name='cartitems',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='items', to='cart.cartorder'),
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cartorder',
            name='owner',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
