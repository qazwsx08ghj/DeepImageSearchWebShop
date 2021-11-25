from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import UserProfileSerializer, UserRegisterSerializer
from django.contrib.auth import get_user_model
# Create your views here.
User = get_user_model()


class UserViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    serializer_class = UserRegisterSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserProfileSerializer
        elif self.action == 'create':
            return UserRegisterSerializer

        return UserRegisterSerializer

    def get_object(self):
        return self.request.user
