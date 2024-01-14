from django.contrib import admin


from .models import Favorite, Rating, Like
# Register your models here.

admin.site.register(Rating)
admin.site.register(Like)