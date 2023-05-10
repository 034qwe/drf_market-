# Generated by Django 4.1.7 on 2023-05-06 17:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_articlesimage_post_alter_articlesimage_image'),
        ('cart', '0005_remove_cart_is_ordered_cartorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartorder',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='item', to='main.articles'),
        ),
    ]