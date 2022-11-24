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
    backdrop_path = models.CharField(max_length=200)
    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def username(self):
        return self.user.username

class Mbti(models.Model):
    title = models.TextField()
    type = models.TextField()
    choice1 = models.TextField()
    choice2 = models.TextField()
    picture1 = models.TextField()
    picture2 = models.TextField()

class Detail(models.Model):
    type = models.TextField(unique=True)
    title = models.TextField()
    sub_title = models.TextField()
    char = models.TextField()
    genres = models.TextField()
    img = models.TextField()
