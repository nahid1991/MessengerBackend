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
def login(request):
    print(request.body)
    try:
        result = json.loads(str(request.body, 'utf-8'))
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
    # print(str(result))
    try:
        user = User.objects.get(username=result['user_id'])
        print("Hello")
        try:
            token = Token.objects.create(user=user)
        except:
            delete_token(user)
            token = Token.objects.create(user=user)
        user_info = UserInformations.objects.get(user=user)
        user_info.access_key = result['access_key']
        user_info.save()

        user_info_serializer = UserInfoSerializer(user_info)
        user_serializer = UserSerializer(user)
        return Response({"token": token.key, "user": user_serializer.data, "user_info": user_info_serializer.data},
                        status=status.HTTP_200_OK)
    except Exception as e:
        try:
            print(e)
            username = result['user_id']
            email = result['email']
            password = '123456'
            user = User.objects.create_user(username, email, password)
            name = result['name'].split(" ")
            user.first_name = name[0]
            if(name[1]):
                user.last_name = name[1]
            user.is_active = True
            user.save()
            user_info = UserInformations.objects.create(name=result['name'],
                                                        email=result['email'],
                                                        user=user,
                                                        created_at=datetime.datetime.now(),
                                                        updated_at=datetime.datetime.now(),
                                                        access_key=result['access_key'])
            user_info_serializer = UserInfoSerializer(user_info)
            user_serializer = UserSerializer(user)
            try:
                token = Token.objects.create(user=user)
            except Exception as e:
                print(e)
            return Response({"token": token.key, "user": user_serializer.data, "user_info": user_info_serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

def delete_token(user):
    try:
        token = Token.objects.get(user=user)
        token.delete()
    except Exception as e:
        print(str(e))

