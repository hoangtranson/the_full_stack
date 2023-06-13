from django import forms
from restaurant.models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'})
        }