# Generated by Django 4.2.1 on 2023-05-30 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0042_client_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='client',
            name='pending',
            field=models.BooleanField(default=True),
        ),
        migrations.DeleteModel(
            name='Status',
        ),
    ]
