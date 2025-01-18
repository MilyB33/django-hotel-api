from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from reservations.models import Reservation

# Create your models here.
class Review(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="reviews")
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(5)],
        help_text="Rating must be between 0 and 5."
    )
    comment = models.TextField(blank=True, help_text="Optional comment about the hotel.")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"Review by {self.user} for {self.reservation} - {self.rating}/5"
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['user', 'reservation']