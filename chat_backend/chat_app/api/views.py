from rest_framework.viewsets import ModelViewSet
from ..models import CustomUser
from .serializers import UserSerializer
# from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status

class UserViewSet(ModelViewSet):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer

class CreateUserView(CreateAPIView):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer

  def perform_create(self, serializer):
    serializer.save()
    return Response({"message": "User created successfully", "user": serializer.data}, status=status.HTTP_201_CREATED)