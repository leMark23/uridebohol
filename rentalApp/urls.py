from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('reservation/', views.reservation_request, name='reservation_request'),
    path('car-list/', views.car_list, name='car_list'),
    path('cars/client-detail/<int:car_id>/', views.car_client_detail, name='car_client_detail'),
    path('motorcycle/client-detail/<int:motorcycle_id>/', views.motorcycle_client_detail, name='motorcycle_client_detail'),
    path('confirmation/<int:pk>/', views.confirmation, name='confirmation'),
    path('client-update/<int:client_id>/', views.client_update, name='client_update'),
    path('motorcycle-list/', views.motorcycle_list, name='motorcycle_list'),
    path('select-vehicle/', views.select_vehicle, name='select_vehicle'),
    path('vehicles/', views.vehicle_list, name='vehicle_list'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
]

