from django import forms
from .models import Flight


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['flight_name', 'flight_type', 'flight_price']
