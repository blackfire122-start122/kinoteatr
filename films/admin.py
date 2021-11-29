from django.contrib import admin
from .models import *

admin.site.register(Films)
admin.site.register(Actor)
admin.site.register(Genre)
admin.site.register(Type)
admin.site.register(Country_film)