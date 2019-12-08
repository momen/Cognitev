from rest_framework import serializers
from rest_framework.authtoken.models import Token

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  "__all__"


class AuthTokenSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
                label="PhoneNumber",
                style={'input_type': 'phonenumber'},
                trim_whitespace=False)
    password = serializers.CharField(
                label="Password",
                style={'input_type': 'password'},
                trim_whitespace=False
    )

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')
        if phone_number and password:
            user = User.objects.get(phone_number=phone_number, password=password)
            if not user:
                msg = 'Unable to log in with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "phone_number" and "password".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class ReAuthTokenSerializer(serializers.Serializer):
    phone_number = serializers.CharField(
                label="PhoneNumber",
                style={'input_type': 'phonenumber'},
                trim_whitespace=False)
    token = serializers.CharField(
                label="Token",
                trim_whitespace=False)

    def validate(self, attrs):
        token = attrs.get('token')
        phone_number = attrs.get('phone_number')
        if token:
            t = Token.objects.get(key=token)
            user = User.objects.get(id=t.user_id, phone_number=phone_number)
            if not user:
                msg = 'Unable to find user with provided credentials.'
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = 'Must include "token".'
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
