# Generated by Django 4.2.1 on 2023-05-22 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0013_alter_client_reservation'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='hotel',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
