from rest_framework.serializers import ModelSerializer
from django.contrib.auth.hashers import make_password
from ..models import CustomUser, Message, ContactList
from rest_framework import serializers

class UserSerializer(ModelSerializer):
  class Meta:
    model = CustomUser
    fields = ('id', 'name', 'email', 'username', 'password',)

  def create(self, validated_data):
    validated_data['password'] = make_password(validated_data.get('password'))
    return super(UserSerializer, self).create(validated_data)

class MessageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Message
    fields = ('id', 'sender', 'receiver', 'content', 'timestamp')


class ContactListSerializer(serializers.ModelSerializer):
  class Meta:
    model = ContactList
    fields = ('id', 'user', 'contact')
