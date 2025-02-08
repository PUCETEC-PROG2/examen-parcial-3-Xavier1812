from django.db import models

class Artist(models.Model):
    name = models.CharField(max_length=100, null=False)
    country = models.CharField(max_length=100, null=False)
        
    def __str__(self):
        return self.name
    
class Album(models.Model):
    title = models.CharField(max_length=100, null=False)
    release_year = models.PositiveIntegerField()
    MUSIC_GENRES = [
        ('HipHop', 'HipHop'),
        ('Rock', 'Rock'),
        ('Reggae', 'Reggae'),
        ('Jazz', 'Jazz'),
        ('Pasillo', 'Pasillo'),
        ('Bachata', 'Bachata'),
    ]
    genre = models.CharField(max_length=30, null=False, choices=MUSIC_GENRES)
    artist = models.ForeignKey(Artist, on_delete=models.SET_NULL, null=True)
    album_cover = models.ImageField(upload_to='examen-parcial-3-Xavier1812/album_manager/media')
    
    def __str__(self):
        return f'{self.title} - {self.release_year}'