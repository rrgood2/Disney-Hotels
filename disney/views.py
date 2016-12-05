from django.shortcuts import render
from disney.models import Hotel
from django.views.generic import ListView

# Create your views here.


class HotelList(ListView):
        model = Hotel

#def hotel_list(request):
#    hotel = HotelTable(Hotel.objects.all())

#    return render(request, 'hotel_list.html', {
 #       'hotel': hotel
  #  })
