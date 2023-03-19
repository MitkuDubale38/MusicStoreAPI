from .models import Music
from .serializers import MusicSerializer
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

class MusicList(generics.ListCreateAPIView):
    queryset = Music.objects.all()
    serializer_class = MusicSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['artist', 'title']
    search_fields = ['artist__artist_name', 'title']
    ordering_fields = ['artist__artist_name', 'title',"created"]