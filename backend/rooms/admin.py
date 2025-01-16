from django.contrib import admin

from .models import Room

class RoomAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'room_type', 'capacity', 'price_per_night', 'is_available')
    list_filter = ('hotel', 'room_type', 'is_available') 

# Register your models here.
admin.site.register(Room)