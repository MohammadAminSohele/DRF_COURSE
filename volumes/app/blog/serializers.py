from rest_framework import serializers

from .models import Article
from django.contrib.auth import get_user_model

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'
        # fields=(title'slug','author','content','published','status')
        # exclude =('created','updated')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields='__all__'