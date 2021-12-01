from django.db import models
from films.models import Films
from django.contrib.auth.models import AbstractUser

class Country(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Country"
		verbose_name_plural = "Country"

class User(AbstractUser):
	age = models.PositiveSmallIntegerField(default=0,null=True,blank=False)
	img = models.ImageField(upload_to="user_img/",default="user_img/default.png",blank=False)
	country = models.ForeignKey(Country, on_delete=models.CASCADE, null=True, blank=False)
	like_films = models.ManyToManyField(Films, blank=False)
	friends = models.ManyToManyField("self", blank=False)
	friends_want_add = models.ManyToManyField("self", blank=False,symmetrical=False)
    
	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = []

	def __str__(self):
		return self.username

	class Meta:
		verbose_name = "User"
		verbose_name_plural = "Users"
