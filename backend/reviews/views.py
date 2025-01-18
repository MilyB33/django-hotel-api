from rest_framework import generics
from rest_framework.exceptions import PermissionDenied

from .models import Review
from reservations.models import Reservation
from .serializers import ReviewSerializer
from api.decorators import auth_required

class ReviewView(
    generics.RetrieveAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView
    ):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'pk'

    def update(self, request, *args, **kwargs):
        self.is_owner()
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        self.is_owner()
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        self.is_owner()
        return super().destroy(request, *args, **kwargs)

    def is_owner(self):
        review = self.get_object()
        user = self.request.user

        if review.user != user and not user.is_staff:
            raise PermissionDenied("You do not have permission to update this review.")

reviews = ReviewView.as_view()

class ReservationReviewView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        reservation_id = self.kwargs.get("reservation_id")

        self.is_reservation_owner()

        return Review.objects.filter(reservation=reservation_id)
    
    def get_serializer_context(self):
        context = super().get_serializer_context()
        
        reservation_id = self.kwargs.get("reservation_id")
        user = self.request.user

        if reservation_id:
            context['reservation_id'] = reservation_id
        
        if user:
            context['user'] = user

        return context
    
    @auth_required
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def is_reservation_owner(self):
        reservation_id = self.kwargs.get("reservation_id")
        user = self.request.user

        reservation =  Reservation.objects.get(id=reservation_id)

        if reservation.user != user and not user.is_staff:
            raise PermissionDenied("You do not have permission to access these reviews.")

    
reservations_reviews = ReservationReviewView.as_view()

class HotelReviewsView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        hotel_id = self.kwargs.get("hotel_id")

        return Review.objects.filter(reservation__room__hotel_id=hotel_id)
    
hotel_reviews = HotelReviewsView.as_view()