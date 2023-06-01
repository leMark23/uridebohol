from django import forms
from django.utils import timezone
from .models import Reservation, Client, Feedback
import datetime
from django.utils import timezone

class ReservationForm(forms.ModelForm):
    start_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    start_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    end_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    end_time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))
    location = forms.ChoiceField(choices=[('Panglao-Airport', 'Panglao-Airport'), ('Tagbilaran-Seaport', 'Tagbilaran-Seaport'), ('Hotel Pick-up', 'Hotel Pick-up')])

    class Meta:
        model = Reservation
        fields = ['location', 'start_date', 'start_time', 'end_date', 'end_time']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'email', 'contact_no', 'hotel', 'message']

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name', 'email', 'message']
