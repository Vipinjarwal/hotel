from django.forms import ModelForm
from .models import Hotel, Customer


class Hotel_Form(ModelForm):
    class Meta:
        model = Hotel
        fields = '__all__'
 
        
class Customer_Form(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'