from django.db import models

class Songs(models.Model):
    id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=255, default='')
    song_title = models.CharField(max_length=255, default='')
    song_year = models.IntegerField(blank=True, null=True)
    song_lyrics = models.TextField()

    class Meta:
        db_table = 'song_lyrics'
