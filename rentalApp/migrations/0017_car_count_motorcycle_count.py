# Generated by Django 4.2.1 on 2023-05-24 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0016_client_motorcycle'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='motorcycle',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]