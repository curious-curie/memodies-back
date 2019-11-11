from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
   
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, related_name="posts",
    on_delete = models.CASCADE, null=True)

    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    album = models.CharField(max_length=100)
    memo = models.TextField()
    artwork = models.TextField()
    preview = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
