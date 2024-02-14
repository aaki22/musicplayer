from django.shortcuts import render
from rest_framework import generics
from .serializer import Room_Serializers
from .models import room

class RoomView(generics.ListAPIView):

    queryset=room.objects.all()
    serializer_class=Room_Serializers