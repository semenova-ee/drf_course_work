from rest_framework import generics
from users.models import User
from users.serializers import UserSerializer, UserCreateSerializer
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsOwner, IsModerator


"""USER generics"""
# ----------------------------------------------------------------

class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    # permission_classes = [IsAuthenticated & IsModerator]


class UserCreateAPIView(generics.CreateAPIView):
    """CREATE User (Регистрация)"""
    serializer_class = UserCreateSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.set_password(serializer.data['password'])
        user.save()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """READ ONE User"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'


class UserUpdateAPIView(generics.UpdateAPIView):
    """UPDATE PUT AND PATCH User"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'


class UserDestroyAPIView(generics.DestroyAPIView):
    """DELETE User"""
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated & IsOwner]
    lookup_field = 'username'