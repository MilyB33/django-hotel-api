from rest_framework import generics
from rest_framework.response import Response
from .models import Room
from .serializers import RoomSerializer

from api.decorators import staff_required

class RoomView(
    generics.RetrieveAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView
    ):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    lookup_field = 'pk'

    @staff_required
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @staff_required
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

room_view = RoomView.as_view()

class HotelRoomsView(
    generics.ListCreateAPIView
    ):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        hotel_id = self.kwargs.get('hotel_id')

        return Room.objects.filter(hotel_id=hotel_id)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        hotel_id = self.kwargs.get('hotel_id')

        if hotel_id:
            context['hotel_id'] = hotel_id

        return context

    @staff_required
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)    
    

hotel_rooms = HotelRoomsView.as_view()