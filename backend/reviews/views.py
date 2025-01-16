from rest_framework import viewsets, generics

from .models import Review
from .serializers import ReviewSerializer

class ReviewView(
    generics.RetrieveAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView
    ):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    lookup_field = 'pk'

reviews = ReviewView.as_view()

class HotelReview(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        hotel_id = self.kwargs.get('hotel_id')

        return Review.objects.filter(hotel=hotel_id)
    
hotel_reviews = HotelReview.as_view()