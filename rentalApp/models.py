from django.db import models
from django.core.validators import RegexValidator
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

class Reservation(models.Model):
    LOCATION_CHOICES = (
        ('', 'Select a location'),
        ('Panglao-Airport', 'Panglao-Airport'),
        ('Tagbilaran-Seaport', 'Tagbilaran-Seaport'),
        ('Hotel Pick-up', 'Hotel Pick-up'),
    )

    location = models.CharField(max_length=100, choices=LOCATION_CHOICES)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateField()
    end_time = models.TimeField()

    def __str__(self):
        return f"Reservation #{self.pk}"

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    seats = models.IntegerField()
    bag = models.CharField(max_length=50)
    mileage = models.CharField(max_length=50, default="Unlimited")
    transmission = models.CharField(max_length=50)
    aircon = models.CharField(max_length=50, default="Air-Conditioned") 
    price = models.DecimalField(max_digits=8, decimal_places=2) 
    image = models.ImageField(upload_to='static/images')
    counter = models.PositiveIntegerField(default=0)
    
    
    def __str__(self):
        return self.name 

class Motorcycle(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cc = models.PositiveIntegerField()
    classtype = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/images')
    counter = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

        
class Client(models.Model):
    reservation = models.OneToOneField(Reservation, on_delete=models.CASCADE, null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True, blank=True)
    motorcycle = models.ForeignKey(Motorcycle, on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    contact_no = models.CharField(max_length=20, validators=[RegexValidator(r'^[0-9]+$')])
    hotel = models.CharField(max_length=100)
    message = models.TextField()
    pending = models.BooleanField(default=True, help_text='Note: Only one of the following fields should be active: Pending, Confirmed, Completed')
    confirmed = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


@receiver(post_save, sender=Client)
def send_confirmation_email(sender, instance, **kwargs):
    if instance.confirmed:
        subject = 'Reservation Confirmation'
        template = 'confirmation_email.html' 
        context = {
            'client_name': instance.first_name,
            'reservation_date': instance.reservation.start_date,
            'reservation_time': instance.reservation.start_time,
        }

        if instance.car:
            context['vehicle_type'] = 'Car'
            context['vehicle_brand'] = instance.car.brand
            context['vehicle_name'] = instance.car.name
        elif instance.motorcycle:
            context['vehicle_type'] = 'Motorcycle'
            context['vehicle_brand'] = instance.motorcycle.brand
            context['vehicle_name'] = instance.motorcycle.name

        message = render_to_string(template, context)
        from_email = 'uridebohol@gmail.com'
        to_email = instance.email

        send_mail(subject, message, from_email, [to_email], html_message=message)


@receiver(post_save, sender=Client)
def update_car_counter(sender, instance, **kwargs):
    if instance.completed and instance.car:
        instance.car.counter += 1
        instance.car.save()

@receiver(post_save, sender=Client)
def update_motorcycle_counter(sender, instance, **kwargs):
    if instance.completed and instance.motorcycle:
        instance.motorcycle.counter += 1
        instance.motorcycle.save()

@receiver(post_save, sender=Client)
def update_pending_status(sender, instance, **kwargs):
    if instance.confirmed and instance.pending:
        instance.pending = False
        instance.save()


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
