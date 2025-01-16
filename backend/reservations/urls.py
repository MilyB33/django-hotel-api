from django.urls import path

from .views import user_reservations

urlpatterns = [
    path('users/<int:user_id>/reservations', user_reservations, name="user-reservations")
]