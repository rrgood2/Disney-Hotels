from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Hotel(models.Model):
	name = models.CharField(max_length = 20)
	address = models.CharField(max_length = 50)
	phone_num = models.CharField(max_length = 12)
	theme = models.CharField(max_length = 20)
	distance = models.SmallIntegerField()
	check_in_time = models.TimeField()
	check_out_time = models.TimeField()
	
	def __unicode__(self):
		return self.name
	
class Room(models.Model):
	hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
	room_num = models.SmallIntegerField()
	capacity = models.SmallIntegerField()
	room_view = models.CharField(max_length = 20)

	class Meta:
		unique_together = ('hotel', 'room_num')
		
	def __unicode__(self):
		return str(self.room_num)
	
class Bed(models.Model):
	hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
	room = models.ForeignKey(Room, on_delete = models.CASCADE)
	
	BED_CHOICES = (
		('TWIN', 'Twin'),
		('FULL', 'Full'),
		('QUEEN', 'Queen'),
		('KING', 'King')
	)
	size = models.CharField(
		max_length = 5,
		choices = BED_CHOICES
	)
	quantity = models.SmallIntegerField()
	
	class Meta:
		unique_together = ('hotel', 'room', 'size')
		
	#def __unicode__(self):
	#	return self.bed_text

class Rate (models.Model):
	hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
	room = models.ForeignKey(Room, on_delete = models.CASCADE)
	date = models.DateField()
	rate = models.SmallIntegerField()
	
	class Meta:
		unique_together = ('hotel', 'room', 'date')	

	#def __unicode__(self):
	#	return self.rate_text

	
class Customer (models.Model):
	cust_id = models.AutoField(primary_key=True, null=False, blank=False)
	name = models.CharField(max_length = 25)
	
	def __unicode__(self):
		return self.cust_id
	
	
class Reservation (models.Model):
	hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
	room = models.ForeignKey(Room, on_delete = models.CASCADE)
	rate = models.ForeignKey(Rate, on_delete = models.CASCADE)
	customer = models.ManyToManyField(Customer)
	num_of_people = models.SmallIntegerField()
	start_date = models.DateField()
	end_date = models.DateField()
	
	#def __unicode__(self):
	#	return self.res_text
	


class Phone (models.Model):
	customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
	phone_num = models.CharField(max_length=12)

	class Meta:
		unique_together = ('customer', 'phone_num')
		
	#def __unicode__(self):
	#	return self.phone_text

class Email (models.Model):
	customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
	email = models.EmailField()

	class Meta:
		unique_together = ('customer', 'email')
		
	#def __unicode__(self):
	#	return self.email_text
		
		
class CreditCard (models.Model):
	customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
	card_num = models.BigIntegerField()
	name = models.CharField(max_length=25)
	
	CARD_TYPE_CHOICES = (
		('VISA', 'Visa'),
		('MASTERCARD', 'MasterCard'),
		('AMERICANEXPRESS', 'American Express'),
		('DISCOVER', 'Discover')
	)
	type = models.CharField(
		max_length=20,
		choices = CARD_TYPE_CHOICES
	)
	
	class Meta:
		unique_together = ('customer', 'card_num')
		
	#def __unicode__(self):
	#	return self.card_text

class Transportation(models.Model):
	hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
	
	TRANSPORT_CHOICES = (
		('COMP_SHUTTLE', 'Complimentary Shuttle'),
		('SHUTTLE_FEE', 'Shuttle (Additional Fee)'),
		('NONE', 'None')
	)
	
	trans_type = models.CharField(
		max_length=15,
		choices = TRANSPORT_CHOICES
	)

	class Meta:
		unique_together = ('hotel', 'trans_type')
		
	def __unicode__(self):
		return self.trans_type
		
class Amenity(models.Model):
	hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
	
	AMENITY_CHOICES = (
		('GIFT_SHOP', 'Gift Shop'),
		('FIT_CENTER', 'Fitness Center'),
		('LAUNDRY', 'Laundromat'),
		('WIFI', 'Wi-Fi'),
		('POOL', 'Swimming Pool'),
		('TICKETS', 'Disneyland Ticket Desk'),
		('ROOM_SERV', 'Room Service')
	)

	
	amenity_type = models.CharField(
		max_length = 25,
		choices = AMENITY_CHOICES
	)

	
	class Meta:
		unique_together = ('hotel', 'amenity_type')
	def __unicode__(self):
		return self.amenity_text
	

class Restaurant (models.Model):
	hotel = models.ForeignKey(Hotel, on_delete = models.CASCADE)
	name = models.CharField(max_length = 25)
	open_hour = models.TimeField()
	close_hour = models.TimeField()
	
	class Meta:
		unique_together = ('hotel', 'name')
	def __unicode__(self):
		return self.name
	
class Dish (models.Model):
	restaurant = models.ForeignKey(Restaurant)
	dish_name = models.CharField(max_length = 20)
	price = models.DecimalField(max_digits = 4, decimal_places = 2)
	
	SIZE_CHOICES = (
		('SMALL', 'Small'),
		('MEDIUM', 'Medium'),
		('LARGE', 'Large')
	)
	
	size = models.CharField(
		max_length = 6,
		choices = SIZE_CHOICES
	)
	
	class Meta:
		unique_together = ('restaurant', 'dish_name', 'size')

	def __unicode__(self):
		return self.dish_name



	
