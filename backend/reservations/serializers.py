from rest_framework import serializers
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    room_details = serializers.CharField(source='room.__str__', read_only=True)
    user_details = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Reservation
        fields = [
            'id', 
            'room', 
            'room_details', 
            'user', 
            'user_details', 
            'check_in_date', 
            'check_out_date', 
            'created_at'
        ]
        read_only_fields = ['id', 'created_at', 'room_details', 'user_details']