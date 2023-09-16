from django.db import models

# Create your models here.


class Hotel(models.Model):
    pass
    

class Customer(models.Model):
    hotel_name = models.CharField(max_length=200)
    hotel_city = models.CharField(max_length=200)
    hotel_address = models.CharField(max_length=100)
    hotel_amenities = models.CharField(max_length=200)
    # hotel_websiteurl = models.URLField(max_length=200)
    person_name = models.CharField(max_length=200)
    email_id = models.EmailField(max_length=200)
    mobile_no = models.CharField(max_length=10)