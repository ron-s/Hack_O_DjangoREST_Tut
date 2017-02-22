from django.db import models

class Songs(models.Model):
    id = models.AutoField(primary_key=True)
    artist_name = models.CharField(max_length=255, default='')
    song_title = models.CharField(max_length=255, default='')
    song_year = models.IntegerField(blank=True, null=True)
    song_lyrics = models.TextField()

    class Meta:
        db_table = 'song_lyrics'

class Movies(models.Model):
    id = models.AutoField(primary_key=True)
    year = models.IntegerField(blank=True, null=True)
    length = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, default='')
    subject = models.CharField(max_length=255, default='')
    actor = models.CharField(max_length=255, default='')
    actress = models.CharField(max_length=255, default='')
    director = models.CharField(max_length=255, default='')
    popularity = models.IntegerField(blank=True, null=True)
    awards = models.BooleanField()
    image = models.CharField(max_length=255, default='')