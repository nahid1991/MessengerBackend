from django.shortcuts import render
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User
from userinformation.models import UserInformations
from userinformation.serializers import UserSerializer, UserInfoSerializer
import json
import datetime

# Create your views here.
@api_view(['POST'])
def facebook_login(request):
    try:
        result = json.loads(str(request.body, 'utf-8'))
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    try:
        user = User.objects.get(username=result['email'])
        try:
            token = Token.objects.create(user=user)
        except:
            delete_token(user)
            token = Token.objects.create(user=user)
        user.last_login = datetime.datetime.now()

        user_info = UserInformations.objects.get(user=user)
        user_info.access_key = result['access_key']
        user_info.social_id = result['user_id']
        user_info.picture = 'https://graph.facebook.com/'+result['user_id']+'/picture?type=large'
        user_info.facebook = True
        user_info.save()

        user.save()

        # user_info_serializer = UserInfoSerializer(user_info)
        # user_serializer = UserSerializer(user)
        return Response(token.key, status=status.HTTP_200_OK)
    except Exception as e:
        try:
            print(e)
            username = result['email']
            email = result['email']
            password = '123456'
            try:
                user = User.objects.create_user(username, email, password)
            except Exception as e:
                print(e)
                return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
            name = result['name'].split(" ")
            user.first_name = name[0]
            if(name[1]):
                user.last_name = name[1]
            user.last_login = datetime.datetime.now()
            user.is_active = True
            user.save()
            UserInformations.objects.create(name=result['name'],
                email=result['email'],
                user=user,
                created_at=datetime.datetime.now(),
                updated_at=datetime.datetime.now(),
                access_key=result['access_key'],
                facebook=True,
                social_id=result['user_id'],
                picture='https://graph.facebook.com/'+result['user_id']+'/picture?type=large')
            # user_info_serializer = UserInfoSerializer(user_info)
            # user_serializer = UserSerializer(user)
            try:
                token = Token.objects.create(user=user)
            except Exception as e:
                print(e)
            return Response(token.key, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

def delete_token(user):
    try:
        token = Token.objects.get(user=user)
        token.delete()
    except Exception as e:
        print(str(e))


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
def get_user_info(request):
    try:
        user_info = UserInformations.objects.get(user=request.user)
        user_info_serializer = UserInfoSerializer(user_info)
        return Response(user_info_serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        print(str(e))
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)