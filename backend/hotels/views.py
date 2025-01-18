from rest_framework import viewsets

from .models import Hotel
from .serializers import HotelSerializer
from api.decorators import staff_required

# Create your views here.
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer
    lookup_field = 'pk'

    @staff_required
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @staff_required
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @staff_required
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)