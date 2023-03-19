from django.urls import path
from .views import MusicList


urlpatterns = [
    path('musics/', MusicList.as_view()),
]