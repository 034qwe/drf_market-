# Generated by Django 4.1.7 on 2023-05-04 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0004_cart_is_ordered'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='is_ordered',
        ),
        migrations.CreateModel(
            name='CartOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartorder_date', models.DateTimeField(auto_now_add=True)),
                ('cart', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='purchase', to='cart.cart')),
            ],
        ),
    ]