from user.serializers import UserSerializer, AuthTokenSerializer
from rest_framework import generics, authentication, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from django.contrib.auth import get_user_model


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UpdateUserView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user


class ListUsersView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)


class DeleteUserView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAdminUser,)


class CreateTokenView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
