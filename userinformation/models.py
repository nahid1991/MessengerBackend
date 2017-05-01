from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInformations(models.Model):
    email = models.CharField(max_length=120, null=True)
    name = models.CharField(max_length=120, null=True)
    access_key = models.CharField(max_length=240, null=True)
    created_at = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(null=True)
    user = models.ForeignKey(User)
    picture = models.CharField(max_length=120, null=True)
    facebook = models.BooleanField(default=False)
    google = models.BooleanField(default=False)
    linkedIn = models.BooleanField(default=False)
    twitter = models.BooleanField(default=False)