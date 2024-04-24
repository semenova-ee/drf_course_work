from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'tg_id')


class UserCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Добавление пользовательских полей в токен
        # token['username'] = user.username
        token['email'] = user.email

        return token