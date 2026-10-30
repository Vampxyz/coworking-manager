from django.shortcuts import render
from .models import Booking, Room, Client


def home_view(request):
    return render(request, "home.html")


def dashboard_view(request):
    bookings = Booking.objects.select_related("room", "client").all()
    clients = Client.objects.all()
    rooms = Room.objects.all()
    context = {
        "bookings": bookings,
        "clients": clients,
        "rooms": rooms,
    }

    return render(request, "dashboard.html", context)
