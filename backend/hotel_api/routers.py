from rest_framework.routers import DefaultRouter

from hotels.views import HotelViewSet
from reservations.views import ReservationViewSet


router = DefaultRouter()

router.register('hotels', HotelViewSet, basename='hotels')
router.register('reservations', ReservationViewSet, basename='reservations')

urlpatterns = router.urls