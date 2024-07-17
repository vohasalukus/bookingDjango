from django.urls import path
from .views import (room_list, detail_information,
                    booking_view, success, profile,
                    delete_room, edit_room, create_room, cancel_booking)

urlpatterns = [
    path('', room_list, name='list_of_rooms'),
    path('hotel-room/<slug:slug>/', detail_information, name='detail_information'),
    path('booking/<slug:slug>/', booking_view, name='booking_room'),
    path('success/', success, name='success'),
    path('profile/', profile, name='profile'),
    path('delete-room/<slug:slug>/', delete_room, name='delete_room'),
    path('edit-room/<slug:slug>', edit_room, name='edit_room'),
    path('create-room/', create_room, name='create_room'),
    path('cancel-booking/<int:booking_id>', cancel_booking, name='cancel_booking')
]
