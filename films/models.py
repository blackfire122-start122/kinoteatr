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
        
class Comments(models.Model):
    user = models.ForeignKey('users.User',on_delete=models.CASCADE)
    comment = models.TextField(null=True,blank=True)
    parent = models.ForeignKey("self",on_delete=models.CASCADE,null=True,blank=True)

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = "comment"
        verbose_name_plural = "comments"

class Films(models.Model):
    name = models.CharField(max_length=30)
    img_film = models.ImageField(upload_to='film_img',default='films/images/default.jpg')
    year = models.PositiveIntegerField(blank=True, null=True)
    country = models.ManyToManyField(Country_film,blank=True)
    actors = models.ManyToManyField(Actor,blank=True)
    genres = models.ManyToManyField(Genre,blank=True)
    typef = models.ForeignKey(Type,on_delete=models.CASCADE, null=True, blank=False)
    description = models.TextField(blank=True)
    comments = models.ManyToManyField(Comments, null=True, blank=True)
    file = models.FileField(upload_to='video/',default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Film"
        verbose_name_plural = "Films"

class Serias(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='video/',default='')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Seria"
        verbose_name_plural = "Serias"

class Sezons(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    serias = models.ManyToManyField(Serias)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sezon"
        verbose_name_plural = "Sezons"


class Serials(models.Model):
    name = models.CharField(max_length=30)
    img_film = models.ImageField(upload_to='film_img',default='films/images/default.jpg')
    year = models.PositiveIntegerField()
    country = models.ManyToManyField(Country_film)
    actors = models.ManyToManyField(Actor)
    genres = models.ManyToManyField(Genre)
    description = models.TextField()
    sezons = models.ManyToManyField(Sezons,blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Serial"
        verbose_name_plural = "Serials"

