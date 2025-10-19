from django.db import models
from django.contrib.auth.models import User
from location.models import Location

class Renter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.user.username

class Booking(models.Model):
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE, related_name='bookings')
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='bookings')
    start_date = models.DateField()
    end_date = models.DateField()
    status = models.CharField(max_length=20, choices=(
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('cancelled', 'Cancelled'),
    ), default='pending')

    def __str__(self):
        return f"{self.renter.user.username} - {self.location.title} ({self.start_date} to {self.end_date})"