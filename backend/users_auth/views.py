from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import ObtainAuthToken as BaseObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from django.forms.models import model_to_dict
from rest_framework import status


from .serializers import RegisterSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

register_view = RegisterView.as_view()

class ObtainAuthToken(BaseObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data.get('token')

        token_instance = Token.objects.get(key=token)
        user = token_instance.user

        user_data = model_to_dict(user)
 
        return Response({
            'token': token,
            'user': user_data
        })
    
obtain_auth_token = ObtainAuthToken.as_view()

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = request.auth

        if token:
            token_instance = Token.objects.get(key=token)
            token_instance.delete()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        
        return Response({"error": "No active token found."}, status=status.HTTP_400_BAD_REQUEST)
    
logout = LogoutView.as_view()