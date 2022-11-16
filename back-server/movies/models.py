from django.db import models
from django.conf import settings

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self) : 
        return self.name


class Movie(models.Model) :
    id = models.IntegerField(primary_key=True)
    genres = models.ManyToManyField(Genre)

    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=200)

    

    def __str__(self):
        return self.title