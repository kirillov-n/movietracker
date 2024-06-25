from django.db import models
from django.contrib.postgres.fields import ArrayField


class Film(models.Model):
    kinopoisk_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    slogan = models.CharField(max_length=800, null=True)
    description = models.CharField(max_length=4000, null=True)
    genres = ArrayField(models.CharField(max_length=20, blank=True))
    rating_imdb = models.FloatField()
    year = models.IntegerField()
    film_length = models.IntegerField(null=True)
    close = ArrayField(models.IntegerField())
