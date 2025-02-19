from rest_framework import serializers

from .models import Article
from django.contrib.auth import get_user_model

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model=Article
        fields='__all__'
        # fields=(title'slug','author','content','published','status')
        # exclude =('created','updated')
    def validate_title(self, value):
        filter_list=['wordpress','c','c++']
        for i in filter_list:
            if i in value:
                raise serializers.ValidationError("Dont say ever these words !! make me so sad")

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=get_user_model()
        fields='__all__'