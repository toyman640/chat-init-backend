from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, CreateUserView, LoginView, MessageViewSet, LogoutView, ContactListViewSet

user_router = DefaultRouter()
user_router.register(r'users', UserViewSet, basename='user')
user_router.register(r'messages', MessageViewSet, basename='message')

contact_router = DefaultRouter()
contact_router.register(r'contact-list', ContactListViewSet, basename='contact-list')

urlpatterns = [
  path('api/', include(user_router.urls)),
  path('api/create-user/', CreateUserView.as_view(), name='create_user'),
  path('login/', LoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout'),
  path('api/', include(contact_router.urls)),
]
