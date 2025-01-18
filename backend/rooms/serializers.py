from rest_framework import serializers

from .models import Room
from hotels.models import Hotel

class RoomSerializer(serializers.ModelSerializer):
    hotel_name = serializers.CharField(source='hotel.name', read_only=True)
    hotel = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Room
        fields = [
            'id', 
            'hotel', 
            'hotel_name', 
            'room_type', 
            'capacity', 
            'price_per_night', 
            'is_available'
        ]
        read_only_fields = ['id', 'hotel_name']


    def create(self, validated_data):
        hotel_id = self.context.get('hotel_id') 

        if not hotel_id:
            raise serializers.ValidationError({'hotel': 'Hotel ID is required.'})
            
        try:
            hotel = Hotel.objects.get(id=hotel_id) 
        except Hotel.DoesNotExist:
            raise serializers.ValidationError({'hotel': 'Invalid hotel ID.'})

        validated_data['hotel'] = hotel  

        return super().create(validated_data)