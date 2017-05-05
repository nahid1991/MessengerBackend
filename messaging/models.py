from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Messages(models.Model):
    sender = models.ForeignKey(User, null=True, related_name='sender')
    receiver = models.ForeignKey(User, null=True, related_name='receiver')
    text = models.TextField(max_length=500)