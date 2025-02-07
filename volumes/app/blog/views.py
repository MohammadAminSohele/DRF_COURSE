from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,DestroyAPIView,RetrieveDestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView

from .models import Article
from .serializers import ArticleSerializer

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