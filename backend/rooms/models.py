from django.db import models
from django.core.validators import MinValueValidator
from hotels.models import Hotel

# Create your models here.
class Room(models.Model):
    SINGLE = 'single'
    DOUBLE = 'double'
    SUITE = 'suite'
    ROOM_TYPES = [
        (SINGLE, 'Single'),
        (DOUBLE, 'Double'),
        (SUITE, 'Suite'),
    ]

    hotel = models.ForeignKey(
        Hotel, 
        on_delete=models.CASCADE,
        related_name='rooms'
    )
    room_type = models.CharField(
        max_length=20,
        choices=ROOM_TYPES,
        default=SINGLE
    )
    capacity = models.PositiveIntegerField(
        validators=[MinValueValidator(1)],
        help_text="Number of people the room can accommodate."
    )
    price_per_night = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        help_text="Price per night for the room."
    )
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_room_type_display()} - {self.hotel.name}"
    
    class Meta:
        ordering = ['price_per_night']
    