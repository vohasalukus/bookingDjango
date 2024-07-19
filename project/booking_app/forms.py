from django import forms
from .models import Booking, HotelRoom


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['entry_date', 'left_date']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['entry_date'].widget = forms.DateInput(attrs={'type': 'date'})
        self.fields['left_date'].widget = forms.DateInput(attrs={'type': 'date'})


class HotelRoomForm(forms.ModelForm):
    class Meta:
        model = HotelRoom
        fields = ['room', 'type_of_room', 'price', 'description', 'image']

