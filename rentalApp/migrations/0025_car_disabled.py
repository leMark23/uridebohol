# Generated by Django 4.2.1 on 2023-05-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0024_car_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='disabled',
            field=models.BooleanField(default=False),
        ),
    ]
