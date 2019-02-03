from django.shortcuts import render

# Create your views here.
from rest_framework import generics

from music.models import Songs
from music.serializers import SongSerializer


class ListSongsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Songs.objects.all()
    serializer_class = SongSerializer