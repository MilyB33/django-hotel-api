from rest_framework import serializers
from django.contrib.auth.models import User

from .models import Review
from reservations.models import Reservation

class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    reservation = serializers.PrimaryKeyRelatedField(read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 
            'user', 
            'user_name', 
            'reservation', 
            'rating', 
            'comment', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'user_name']

    def create(self, validated_data):
        reservation_id = self.context.get('reservation_id')
        user_ = self.context.get('user')

        if not user_:
            raise serializers.ValidationError({"user": "User id is required."})

        if not reservation_id:
            raise serializers.ValidationError({"reservation": "Reservation id is required."})
        
        try:
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            raise serializers.ValidationError({"reservation": "Invalid reservation id"})

        try:
            user = User.objects.get(id=user_.id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"user": "Invalid user."})
        
        validated_data['user'] = user
        validated_data['reservation'] = reservation

        return super().create(validated_data)