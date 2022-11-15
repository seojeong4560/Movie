from django.db import models
from django.conf import settings

# Create your models here.
class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self) : # admin 페이지에서 편하게 보기 위함
        return self.name


class Movie(models.Model) :
    id = models.IntegerField(primary_key=True)
    genres = models.ManyToManyField(Genre)

    # title = models.CharField(max_length=100)
    # release_date = models.DateField()
    # vote_count = models.IntegerField()
    # vote_average = models.FloatField()
    # overview = models.TextField()
    # poster_path = models.CharField(max_length=200)

    title = models.CharField(max_length=100)
    release_date = models.DateField()
    popularity = models.FloatField()
    vote_average = models.FloatField()
    overview = models.TextField()
    poster_path = models.CharField(max_length=500)
    # genres = models.ManyToManyField(Genre)
    

    def __str__(self):
        return self.title