from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# ListAPIView,RetrieveAPIView,DestroyAPIView,RetrieveDestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView

from rest_framework.permissions import IsAdminUser

from .models import Article
from django.contrib.auth.models import User
from .serializers import ArticleSerializer,UserSerializer
from .permissions import IsSuperUser

# Create your views here.

class ArticleList(ListCreateAPIView):
    queryset=Article.objects.filter(status=True)
    serializer_class=ArticleSerializer

# class ArticleList(ListCreateAPIView):
#     queryset=Article.objects.filter(status=True)
#     serializer_class=ArticleSerializer

class ArticleDetail(RetrieveUpdateDestroyAPIView):
    queryset=Article.objects.filter(status=True)
    serializer_class=ArticleSerializer
    lookup_field='slug'


class UserList(ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsSuperUser,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsSuperUser,)