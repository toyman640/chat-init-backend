from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here.
class CustomUser(AbstractUser):
  name = models.CharField(max_length=255, blank=True, null=True)

  def __str__(self):
    return self.username


class Message(models.Model):
  sender = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='sent_messages')
  receiver = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='received_messages')
  content = models.TextField()
  timestamp = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f'{self.sender.username} to {self.receiver.username}: {self.content}'