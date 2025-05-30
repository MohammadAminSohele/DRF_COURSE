from rest_framework import serializers

from .models import Article
from django.contrib.auth import get_user_model

from drf_dynamic_fields import DynamicFieldsMixin

class ArticleSerializer(DynamicFieldsMixin,serializers.ModelSerializer):
    def get_author(self,obj):
        # return obj.author.username
        return {
            'Username':obj.author.username,
            'FirstName':obj.author.first_name,
            'LastName':obj.author.last_name,
        }
    author=serializers.SerializerMethodField('get_author')
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