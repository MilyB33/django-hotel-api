from rest_framework import serializers

from .models import Review

class ReviewSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.username', read_only=True)
    hotel_name = serializers.CharField(source='hotel.name', read_only=True)

    class Meta:
        model = Review
        fields = [
            'id', 
            'user', 
            'user_name', 
            'hotel', 
            'hotel_name', 
            'rating', 
            'comment', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at', 'user_name', 'hotel_name']