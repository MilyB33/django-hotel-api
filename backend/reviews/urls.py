from django.urls import path

from .views import reviews, reservations_reviews, hotel_reviews

urlpatterns = [
    path('reviews/<int:pk>/', reviews, name='reviews'),
    path('reservations/<int:reservation_id>/reviews/', reservations_reviews, name='reservations-reviews'),
    path('hotels/<int:hotel_id>/reviews/', hotel_reviews, name="hotel-reviews")
]