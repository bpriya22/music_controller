from django.shortcuts import render
from rest_framework import generics
from .models import Room
from .serializers import RoomSerializer
# Create your views here.
#to write end points..


#this is a API view
class RoomView(generics.CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

