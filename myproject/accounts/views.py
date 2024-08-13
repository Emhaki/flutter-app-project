from django.shortcuts import render
from .serializer import UserSerializer
from .models import CustomUser
from rest_framework import generics

# 회원가입
class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer