# Generated by Django 4.0.3 on 2022-03-19 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures_api', '0009_cart'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
        migrations.AlterField(
            model_name='review',
            name='comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]