from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.viewsets import ModelViewSet
from ..models import CustomUser
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

class CustomObtainAuthToken(ObtainAuthToken):
  def post(self, request, *args, **kwargs):
    serializer = self.serializer_class(data=request.data, context={'request': request})
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key, 'user_id': user.pk, 'username': user.username})

class UserViewSet(ModelViewSet):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer

class CreateUserView(CreateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer

  def perform_create(self, serializer):
    serializer.save()
    return Response({"message": "User created successfully", "user": serializer.data}, status=status.HTTP_201_CREATED)\

class LoginView(CustomObtainAuthToken):
  pass