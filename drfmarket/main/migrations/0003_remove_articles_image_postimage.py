# Generated by Django 4.1.7 on 2023-04-19 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_articles_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='image',
        ),
        migrations.CreateModel(
            name='PostImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('alt', models.CharField(blank=True, max_length=200, null=True)),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.articles')),
            ],
            options={
                'verbose_name': 'Image',
                'verbose_name_plural': 'Images',
                'abstract': False,
            },
        ),
    ]
