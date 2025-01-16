from  rest_framework import viewsets, generics

from .models import Reservation
from .serializers import ReservationSerializer

# Create your views here.
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'pk'

class UserReservationView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


    def get_queryset(self):
        user_id = self.kwargs.get('user_id')

        return Reservation.objects.filter(user=user_id)
    
user_reservations = UserReservationView.as_view()
