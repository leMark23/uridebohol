# Generated by Django 4.2.1 on 2023-05-29 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rentalApp', '0037_remove_client_completed_remove_client_pending_and_more'),
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
        migrations.AlterField(
            model_name='client',
            name='reservation',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='rentalApp.reservation'),
        ),
        migrations.DeleteModel(
            name='ReservationStatus',
        ),
    ]
