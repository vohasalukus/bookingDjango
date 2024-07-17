from django.contrib import admin
from .models import HotelRoom, Booking


class HotelRoomAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('room',)}


admin.site.register(HotelRoom, HotelRoomAdmin)
admin.site.register(Booking)

