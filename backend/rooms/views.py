from rest_framework import generics

from .models import Room
from .serializers import RoomSerializer

class RoomView(
    generics.RetrieveAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView
    ):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'pk'

room_view = RoomView.as_view()

class HotelRoomsView(
    generics.ListCreateAPIView
    ):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        hotel_id = self.kwargs.get('hotel_id')

        return Room.objects.filter(hotel_id=hotel_id)
        
    

hotel_rooms = HotelRoomsView.as_view()