from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    '''Сериализатор пользователя'''

    class Meta:
        model = User
        fields = ('id', 'username', 'telegram', 'first_name', 'last_name', 'is_active',)


class UserCreateSerializer(serializers.Serializer):
    '''Сериализатор создания пользователя'''

    def create(self, validated_data):
        password = validated_data.get('password')

        # Hash the password before saving
        if password:
            hashed_password = make_password(password)
            validated_data['password'] = hashed_password

        user = super().create(validated_data)
        return user

    def update(self, instance, validated_data):
        password = validated_data.get('password')

        # Hash the password before saving
        if password:
            hashed_password = make_password(password)
            validated_data['password'] = hashed_password

        user = super().update(instance, validated_data)
        return user

    class Meta:
        model = User
        fields = ('email', 'password')
        ref_name = 'CustomUserSerializer'