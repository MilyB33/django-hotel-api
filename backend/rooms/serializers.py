from rest_framework import serializers

from .models import Room

class RoomSerializer(serializers.ModelSerializer):
    hotel_name = serializers.CharField(source='hotel.name', read_only=True)

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
            hotel_id = self.context['view'].kwargs['hotel_id']
            validated_data['hotel'] = hotel_id
            return super().create(validated_data)