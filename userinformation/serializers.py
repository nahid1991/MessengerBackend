from django.contrib.auth.models import User
from userinformation.models import UserInformations
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class UserInfoSerializer(serializers.ModelSerializer):
    user = UserSerializer(source='get_user_info', read_only=True)
    class Meta:
        model = UserInformations
        fields = ('id', 'name', 'email', 'access_key', 'picture', 'facebook', 'google', 'linkedIn', 'twitter', 'user')