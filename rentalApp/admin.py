from django.contrib import admin
from .models import Reservation, Car, Client, Motorcycle, Feedback

admin.site.register(Reservation)
admin.site.register(Car)
admin.site.register(Client)
admin.site.register(Motorcycle)
admin.site.register(Feedback)

admin.site.site_header = "U-Ride Admin"
admin.site.site_title = "U-ride Admin Portal"
admin.site.index_title = "Welcome to U-ride Rental Services Admin Portal"