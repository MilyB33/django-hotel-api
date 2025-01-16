from django.urls import path

from .views import register_view, obtain_auth_token, logout

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', logout, name="logout")
]