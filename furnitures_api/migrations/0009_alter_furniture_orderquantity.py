# Generated by Django 4.0.3 on 2022-03-20 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures_api', '0008_alter_cart_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='furniture',
            name='orderQuantity',
            field=models.IntegerField(default=1),
        ),
    ]
