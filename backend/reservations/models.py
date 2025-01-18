from django.db import models
from django.core.exceptions import ValidationError

from rooms.models import Room

# Create your models here.
class Reservation(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reservations')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.pk:
            original = Reservation.objects.get(pk=self.pk)
            if original.check_in_date != self.check_in_date or original.check_out_date != self.check_out_date:
                if self.check_in_date >= self.check_out_date:
                    raise ValidationError({"error": "Check-out date must be after check-in date."})
                
                overlapping_reservations = Reservation.objects.filter(
                    room=self.room,
                    check_in_date__lt=self.check_out_date,
                    check_out_date__gt=self.check_in_date
                ).exclude(pk=self.pk).exists()

                if overlapping_reservations:
                     raise ValidationError({"error": "The room is already booked for the selected date."})
                
        else:
            if self.check_in_date >= self.check_out_date:
                raise ValidationError({"error": "Check-out date must be after check-in date."})
            
            overlapping_reservations = Reservation.objects.filter(
                room=self.room,
                check_in_date__lt=self.check_out_date,
                check_out_date__gt=self.check_in_date
            ).exists()

            if overlapping_reservations:
                raise ValidationError({"error": "The room is already booked for the selected date."})
        
    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"Reservation for {self.room} by {self.user} from {self.check_in_date} to {self.check_out_date}"
    
    class Meta:
        ordering = ['check_in_date']