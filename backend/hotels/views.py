from rest_framework import viewsets
from rest_framework.decorators import action
from django.http import JsonResponse

from .models import Hotel
from rooms.models import Room
from .serializers import HotelSerializer
from rooms.serializers import RoomSerializer

# Create your views here.
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    lookup_field = 'pk'


