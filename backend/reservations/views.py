from  rest_framework import viewsets, generics

from api.decorators import staff_required, check_ownership
from .models import Reservation
from .serializers import ReservationSerializer

# Create your views here.
class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'pk'

    @staff_required
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        
        user = self.request.user

        if user:
            context['user'] = user

        return context
    
    @check_ownership
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
    
    @check_ownership
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    @check_ownership
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @check_ownership
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)


class UserReservationView(generics.ListAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer


    def get_queryset(self):
        print(self)
        user = self.request.user

        if user.is_authenticated:
            return self.queryset.filter(user=user)
        return self.queryset.none()
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        
        user = self.request.user

        if user:
            context['user'] = user

        return context
        
    def list(self, request, *args, **kwargs):
        print("list")
        return super().list(request, *args, **kwargs)

    
user_reservations = UserReservationView.as_view()
