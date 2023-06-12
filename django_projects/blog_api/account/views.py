from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from . import serializer

from dj_rest_auth.views import LogoutView

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.RegisterSerializer

class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated,)

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserListSerializer
    permission_classes = (permissions.IsAuthenticated, )

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializer.UserDetailSerializer
    permission_classes = (permissions.IsAuthenticated, )