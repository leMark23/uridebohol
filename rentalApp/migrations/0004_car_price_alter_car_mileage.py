# Generated by Django 4.2.1 on 2023-05-19 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0003_car'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='price',
            field=models.DecimalField(decimal_places=2, default='0.00', max_digits=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.CharField(default='Unlimited', max_length=50),
        ),
    ]