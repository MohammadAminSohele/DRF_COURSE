from rest_framework import serializers

from .models import Article
from django.contrib.auth.models import User

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'
        # fields=(title'slug','author','content','published','status')
        # exclude =('created','updated')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'