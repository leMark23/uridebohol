# Generated by Django 4.2.1 on 2023-05-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0002_alter_reservation_location'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('seats', models.IntegerField()),
                ('bag', models.CharField(max_length=50)),
                ('mileage', models.CharField(max_length=50)),
                ('transmission', models.CharField(max_length=50)),
                ('aircon', models.CharField(default='Air-Conditioned', max_length=50)),
                ('image', models.ImageField(upload_to='static/images')),
            ],
        ),
    ]
