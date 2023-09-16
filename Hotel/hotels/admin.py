from django.contrib import admin
from .models import Customer 

# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('hotel_name', 'hotel_city', 'hotel_address', 'hotel_amenities', 'person_name','email_id', 'mobile_no')

admin.site.register(Customer,CustomerAdmin)

