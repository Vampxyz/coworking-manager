from django.shortcuts import render
from .models import Booking, Room, Client

def dashboard_view(request):
    bookings = Booking.objects.select_related('client', 'room').all()
    rooms = Room.objects.all()
    clients = Client.objects.all()

    context = {
        'bookings': bookings,
        'rooms': rooms,
        'clients': clients,
        'total_bookings': bookings.count(),
    }
    
    return render(request, 'bookings/dashboard.html', context)