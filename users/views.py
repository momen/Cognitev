from django.http import HttpResponse
from django.forms.models import model_to_dict
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from users.serializers import UserSerializer, AuthTokenSerializer, ReAuthTokenSerializer
from users.models import User



class UserCreation(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = AuthTokenSerializer(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user_id=user.id)
        return Response({
            'token': token.key,
        })


class ReAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = ReAuthTokenSerializer(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return HttpResponse(user)