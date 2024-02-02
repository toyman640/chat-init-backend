from django.contrib import admin
from .models import CustomUser, Message, ContactList

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Message)
admin.site.register(ContactList)
