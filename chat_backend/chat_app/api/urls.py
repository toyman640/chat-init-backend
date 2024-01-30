from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CreateUserView, LoginView, MessageViewSet

user_router = DefaultRouter()
user_router.register(r'users', UserViewSet, basename='user')
user_router.register(r'messages', MessageViewSet, basename='message')

urlpatterns = [
  path('api/', include(user_router.urls)),
  path('api/create-user/', CreateUserView.as_view(), name='create_user'),
  path('login/', LoginView.as_view(), name='login'),
]
