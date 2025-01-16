from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Hotel
from rooms.serializers import RoomSerializer

class HotelSerializer(serializers.ModelSerializer):
    rooms = RoomSerializer(many=True, read_only=True)

    class Meta:
        model = Hotel
        fields = [
            'pk',
            'name',
            'location',
            'description',
            'created_at',
            'average_rating',
            'rooms'
        ]