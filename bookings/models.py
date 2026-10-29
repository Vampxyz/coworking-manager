from django.db import models


# Create your models here.
class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone_number}"

class Room(models.Model):
    ROOM_TYPES = [
        ('Private', 'Private Room'),
        ('Meeting', 'Meeting Room'),
        ('Event', 'Event Room'),
        ('Coworking', 'Coworking Space'),
    ]

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    room_type = models.CharField(choices=ROOM_TYPES, max_length=20)
    capacity = models.IntegerField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.name} - {self.room_type} - Capacity: {self.capacity} - Price: ${self.price_per_hour} - Available: {'Yes' if self.availability else 'No'}"

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()

    def __str__(self):
        return f"{self.client.name} - {self.date} {self.time} | Sala: {self.room.name}"