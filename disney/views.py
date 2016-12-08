from django.shortcuts import render
from disney.models import Hotel
from disney.models import Reservation
from django.views.generic import ListView

# Create your views here.

class HotelList(ListView):
        model = Hotel

class ReservationList(ListView):
        model = Reservation
