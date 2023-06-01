# Generated by Django 4.2.1 on 2023-05-19 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(choices=[('Panglao-Airport', 'Panglao-Airport'), ('Tagbilaran-Seaport', 'Tagbilaran-Seaport'), ('Hotel Pick-up', 'Hotel Pick-up')], max_length=100)),
                ('start_date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_date', models.DateField()),
                ('end_time', models.TimeField()),
            ],
        ),
    ]