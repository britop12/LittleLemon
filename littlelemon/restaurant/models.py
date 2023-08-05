from django.db import models

# Create your models here.
class Booking(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    Booking_date = models.DateField()
    
class Menu(models.Model):
    ID = models.AutoField(primary_key=True)
    titte = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()