# Generated by Django 4.0.3 on 2022-03-19 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('furnitures_api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='furniture',
            name='rating',
        ),
    ]
