from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=100)
    slug=models.SlugField()
    author=models.ForeignKey(User,null=True,on_delete=models.CASCADE)
    content=models.TextField()
    published=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    def __str__(self):
        return self.title