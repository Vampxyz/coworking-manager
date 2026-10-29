from django.contrib import admin

from bookings.models import Booking, Client, Room

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone_number')
    search_fields = ('name', 'email')
    
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'room_type', 'capacity', 'price_per_hour', 'availability')
    list_filter = ('room_type', 'availability')
    search_fields = ('name',)
    
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('client', 'room', 'date', 'time', 'duration')
    list_filter = ('date', 'time')
    search_fields = ('client__name', 'room__name')