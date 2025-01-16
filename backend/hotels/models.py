from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    @property
    def average_rating(self):
        pass

    def __str__(self):
        return f"{self.name} - {self.average_rating or 'No rating'}"