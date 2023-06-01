from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ReservationForm, ClientForm, FeedbackForm
from .models import Reservation, Car, Client, Motorcycle, Feedback
import datetime
from django.http import JsonResponse
from django.core.mail import send_mail
from django.urls import reverse


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST': 
        form = FeedbackForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('contact')
    else:
        form = FeedbackForm()
    
    return render(request, 'contact.html', {'form': form})

def reservation_request(request):
    if request.method == 'POST':
        today = datetime.datetime.now().strftime('%Y-%m-%dT%H:%M')
        form = ReservationForm(request.POST or None)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date'] 
            if end_date <= start_date:
                return JsonResponse({'success': False, 'message': 'Return date shouldnt be before pick up date.'})
            else:
                reservation = form.save(commit=False)
                reservation.save()
                return JsonResponse({'success': True, 'message': 'Your reservation has been saved.'})
        else:
            return JsonResponse({'success': False, 'message': 'Return date shouldnt be before pick up date.'})
    else:
        form = ReservationForm()

    return render(request, 'home.html', {'form': form}) 
 
def select_vehicle(request):
    if request.method == 'POST':
        vehicle_type = request.POST.get('vehicle_type')
        if vehicle_type == 'car':
            return redirect('car_list')
        elif vehicle_type == 'motorcycle':
            return redirect('motorcycle_list')
        else:
            messages.error(request, 'Invalid vehicle type.')
    return render(request, 'select_vehicle.html') 

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'car_list': cars})

def vehicle_list(request):
    cars = Car.objects.all()
    motorcycles = Motorcycle.objects.all()
    context = {
        'cars': cars,
        'motorcycles': motorcycles,
    }
    return render(request, 'vehicle_list.html', context)

def motorcycle_list(request):
    motorcycles = Motorcycle.objects.all()
    return render(request, 'motorcycle_list.html', {'motorcycle_list': motorcycles})

def car_client_detail(request, car_id):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            car = get_object_or_404(Car, id=car_id)

            if car.counter > 0:
                car.counter -= 1
                car.save()

            client.car = car
            client.save()

            reservation = Reservation.objects.latest('id')
            client.reservation = reservation
            client.pending = True 
            client.save()

            form = ClientForm()
            return redirect('confirmation', pk=client.pk)
    else:
        form = ClientForm()

    return render(request, 'client_details.html', {'form': form})

def motorcycle_client_detail(request, motorcycle_id):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            motorcycle = get_object_or_404(Motorcycle, id=motorcycle_id)

            if motorcycle.counter > 0:
                motorcycle.counter -= 1
                motorcycle.save()


            client.motorcycle = motorcycle
            client.save()

            reservation = Reservation.objects.latest('id')
            client.reservation = reservation
            client.pending = True 
            client.save()

            form = ClientForm()
            return redirect('confirmation', pk=client.pk)
    else:
        form = ClientForm()

    return render(request, 'client_details.html', {'form': form})

def client_update(request, client_id):
    client = get_object_or_404(Client, id=client_id)
    car = client.car  # Fetch the associated car
    motorcycle = client.motorcycle  # Fetch the associated motorcycle

    if request.method == 'POST':
        form = ClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('confirmation', pk=client.pk)
    else:
        form = ClientForm(instance=client)

    context = {
        'form': form,
        'client': client,
        'car': car,  
        'motorcycle': motorcycle,
    }
    return render(request, 'client_update.html', context)

def confirmation(request, pk):
    client = get_object_or_404(Client, pk=pk)
    car = client.car
    motorcycle = client.motorcycle
    reservation = client.reservation

    if request.method == 'POST':
        form = ClientForm()
    else:
        form = ClientForm()

    total_duration = reservation.end_date - reservation.start_date
    total_duration_days = total_duration.days

    if car: 
        total_amount = car.price * total_duration_days
    elif motorcycle:
        total_amount = motorcycle.price * total_duration_days
    else:
        total_amount = 0    

    context = {
        'client': client,
        'car': car,
        'motorcycle': motorcycle,
        'reservation': reservation,
        'form': form,
        'total_duration_days': total_duration_days,
        'total_amount': total_amount,
    }
    return render(request, 'confirmation.html', context)
