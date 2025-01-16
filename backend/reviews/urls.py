from django.urls import path

from .views import reviews, hotel_reviews

urlpatterns = [
    path('rooms/', reviews, name='reviews'),
    path('hotels/<int:hotel_id>/reviews', hotel_reviews, name='hotel-reviews'),
]