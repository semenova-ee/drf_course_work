from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class UserCreateSerializer(serializers.Serializer):

    # def create(self, validated_data):
    #     password = validated_data.get('password')
    #
    #     # Hash the password before saving
    #     if password:
    #         hashed_password = make_password(password)
    #         validated_data['password'] = hashed_password
    #
    #     user = super().create(validated_data)
    #     return user
    #
    # def update(self, instance, validated_data):
    #     password = validated_data.get('password')
    #
    #     # Hash the password before saving
    #     if password:
    #         hashed_password = make_password(password)
    #         validated_data['password'] = hashed_password
    #
    #     user = super().update(instance, validated_data)
    #     return user

    class Meta:
        model = User
        fields = ('email', 'password',)

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name',)
