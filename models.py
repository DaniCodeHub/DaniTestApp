from django.db import models
from django.utils import timezone
import datetime


# Create your models here.

class TodoItem(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

class Broker(models.Model):
    broker_name = models.CharField(max_length=100)
    established = models.BooleanField(default=False)

class Seller(models.Model):
    seller_name= models.CharField(max_length=100)
    seller_established = models.BooleanField(default=False)
    #startdate = models.DateField(default=timezone.now())
    
    def __str__(self):
        return self.seller_name

    #def broker_status(self):
        #"Shows how long the employee has been with the company"
        #import datetime

        #if self.startdate <= datetime.date(2000, 1, 1):
            #return "Veteran Seller"
        #elif self.startdate <= datetime.date(2010, 1, 1):
            #return "Recently Hired Seller"
        #else:
            #return "New Seller"

        # @property
        # def Broker_name(self):
        # "Return the employee's full name."
        # return f"{self.first_name} {self.last_name}"
