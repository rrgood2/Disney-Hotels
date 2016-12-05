from django.contrib import admin

# Register your models here.
from .models import Hotel
admin.site.register(Hotel)

from .models import Room
admin.site.register(Room)

from .models import Bed
admin.site.register(Bed)

from .models import Rate
admin.site.register(Rate)

from .models import Customer
admin.site.register(Customer)

from .models import Reservation
admin.site.register(Reservation)

from .models import Phone
admin.site.register(Phone)

from .models import Email
admin.site.register(Email)

from .models import CreditCard
admin.site.register(CreditCard)

from .models import Transportation
admin.site.register(Transportation)

from .models import Amenity
admin.site.register(Amenity)

from .models import Restaurant
admin.site.register(Restaurant)

from .models import Dish
admin.site.register(Dish)



