from django import forms
from .models import Booking, HotelRoom


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['entry_date', 'left_date']


class HotelRoomForm(forms.ModelForm):
    class Meta:
        model = HotelRoom
        fields = ['room', 'type_of_room', 'price', 'description', 'image']

