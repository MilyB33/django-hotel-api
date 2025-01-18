from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import PermissionDenied
from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
    room_details = serializers.CharField(source='room.__str__', read_only=True)
    user_details = serializers.CharField(source='user.username', read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only=True)

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

    def create(self, validated_data):
        user_ = self.context.get('user')

        if not user_:
            raise serializers.ValidationError({"user": "User id is required."})
        
        try:
            user = User.objects.get(id=user_.id)
        except User.DoesNotExist:
            raise serializers.ValidationError({"user": "Invalid user."})
        
        validated_data['user'] = user

        return super().create(validated_data)



    