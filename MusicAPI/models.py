from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100,blank=False,null=False)
    def __str__(self):
        return self.name


class Artist(models.Model):
    artist_name = models.CharField(max_length=100, blank=False)
    artist_photo = models.ImageField(upload_to="ArtistPhotos/",null = True,blank = True)
    created_on = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.artist_name

    class Meta:
        ordering = ('artist_name',)


class Music(models.Model):
    
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=100, blank=False,null=False)
    audio_file = models.FileField(upload_to="musics/",null = False,blank = False)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, blank = True, null = True)
    created = models.DateTimeField(auto_now_add=True)
    cover = models.ImageField(upload_to="covers/",null = True,blank = True)
    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.title



