from functools import wraps
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied

def staff_required(func):
    @wraps(func)
    def inner(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return Response({"message": 'Not allowed.'}, status=status.HTTP_403_FORBIDDEN)
        return func(self, request, *args, **kwargs)
    return inner

def auth_required(func):
    @wraps(func)
    def inner(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return Response({"message": "Authenticated credentials were not provided.",},status=status.HTTP_401_UNAUTHORIZED)
        return  func(self, request, *args, **kwargs)
    return inner

def check_ownership(func):
    @wraps(func)
    def inner(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.user != request.user:
            raise PermissionDenied("YOu are not allowed to perform this action.")
        
        return func(self, request, *args, **kwargs)
    return inner