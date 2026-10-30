from django.db import models


# Create your models here.
class Client(models.Model):    
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)
    
    def __str__(self):
        return f"{self.name} - {self.email}"

class Room(models.Model):
    ROOM_TYPES = [
        ('Private', 'Private Room'),
        ('Meeting', 'Meeting Room'),
        ('Event', 'Event Room'),
        ('Coworking', 'Coworking Space'),
    ]
    name = models.CharField(max_length=100, blank=False)
    room_type = models.CharField(choices=ROOM_TYPES, max_length=20)
    capacity = models.IntegerField()
    price_per_hour = models.DecimalField(max_digits=10, decimal_places=2)
    availability = models.BooleanField(default=True)
    
    @property
    def vacancies(self):
        booked_counts = self.bookings.count()
        
        remaining = self.capacity - booked_counts

        return remaining if remaining > 0 else 0
    
    def __str__(self):
        return f"{self.name} - Vagas restantes: {self.vacancies} | Tipo: {self.room_type} | Preço/hora: R${self.price_per_hour}"

class Booking(models.Model):    
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    
    date = models.DateField()
    time = models.TimeField()
    duration = models.DurationField()

    def __str__(self):
        return f"{self.client.name} - {self.date} {self.time} | Sala: {self.room.name}"