# Generated by Django 4.2.1 on 2023-05-22 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0010_alter_client_reservation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='car',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rentalApp.car'),
        ),
    ]