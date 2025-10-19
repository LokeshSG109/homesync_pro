from django.db import models
from owner.models import Owner

class Location(models.Model):
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name='properties')
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} - {self.address}"