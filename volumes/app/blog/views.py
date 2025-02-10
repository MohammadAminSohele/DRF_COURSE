from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
# ListAPIView,RetrieveAPIView,DestroyAPIView,RetrieveDestroyAPIView,UpdateAPIView,RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response


from rest_framework.permissions import IsAuthenticated
# IsAdminUser

from .models import Article
from django.contrib.auth.models import User
from .serializers import ArticleSerializer,UserSerializer
from .permissions import IsSuperUser,IsAuthorOrReadOnly,IsStaffOrReadOnly,IsSuperUserOrStaffReadOnly

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
    permission_classes=(IsStaffOrReadOnly,IsAuthorOrReadOnly)


class UserList(ListCreateAPIView):
    # def get_queryset(self):
    #     print('----------------')
    #     print(self.request.user)
    #     print(self.request.auth)
    #     print('----------------')
    #     return User.objects.all()
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsSuperUserOrStaffReadOnly,)

class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsSuperUserOrStaffReadOnly,)

class RevokeToken(APIView):
    permission_classes=(IsAuthenticated,)
    def get(self, request):
        return Response({'method':'get'})
    def put(self, request):
        return Response({'method':'put'})
    def delete(self, request):
        return Response({'method':'delete'})
    def post(self, request):
        return Response({'method':'post'})