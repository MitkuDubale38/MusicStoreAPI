from .models import Music,Artist,Genre
from rest_framework import serializers

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ["id","artist_name"]

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ["name"]


class MusicSerializer(serializers.ModelSerializer):
    artist = ArtistSerializer()
    genre = GenreSerializer()
    class Meta:
        model = Music
        fields = ["artist","title","audio_file","genre","created","cover"]
        # depth = 1