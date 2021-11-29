from django.db import models

class Country_film(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Country_film"
        verbose_name_plural = "Country_films"

class Actor(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to="actors/",default="actors/default.png")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Actor"
        verbose_name_plural = "Actors"


class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Genre"
        verbose_name_plural = "Genres"

class Type(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Type"
        verbose_name_plural = "Types"

class Films(models.Model):
    name = models.CharField(max_length=30)
    img_film = models.ImageField(upload_to='film_img',default='films/images/default.jpg')
    year = models.PositiveIntegerField()
    country = models.ManyToManyField(Country_film)
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    typef = models.ManyToManyField(Type)
    description = models.TextField()
    file = models.FileField(upload_to='video/',default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"
