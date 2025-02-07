from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,DestroyAPIView,RetrieveDestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView

from .models import Article
from django.contrib.auth.models import User
from .serializers import ArticleSerializer,UserSerializer

# Create your views here.

class ArticleList(ListAPIView):
    queryset=Article.objects.filter(status=True)
    serializer_class=ArticleSerializer

# class ArticleList(ListCreateAPIView):
#     queryset=Article.objects.filter(status=True)
#     serializer_class=ArticleSerializer

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.filter(status=True)
    serializer_class=ArticleSerializer


class UserList(ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer