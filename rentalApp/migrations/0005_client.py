# Generated by Django 4.2.1 on 2023-05-19 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0004_car_price_alter_car_mileage'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact_no', models.CharField(max_length=20)),
                ('message', models.TextField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rentalApp.car')),
            ],
        ),
    ]