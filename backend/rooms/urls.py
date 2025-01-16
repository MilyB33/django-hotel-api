from django.urls import path

from .views import hotel_rooms, room_view

urlpatterns = [
    path('rooms/<int:pk>/', room_view, name='rooms'),
    path('hotels/<int:hotel_id>/rooms/', hotel_rooms, name='hotel-rooms'),
]