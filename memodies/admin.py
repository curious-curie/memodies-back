from django.contrib import admin
from .models import Post, Playlist
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Post)
admin.site.register(Playlist)