from django.urls import path

from .views import user_reservations

urlpatterns = [
    path('user/reservations/', user_reservations, name="my-reservations")
]