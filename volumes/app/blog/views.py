from django.shortcuts import render

from django.contrib.auth.models import User

from rest_framework.viewsets import ModelViewSet

from .models import Article
from .serializers import ArticleSerializer,UserSerializer
from .permissions import IsAuthorOrReadOnly,IsStaffOrReadOnly,IsSuperUserOrStaffReadOnly

# Create your views here.

class ArticleViewSet(ModelViewSet):
    queryset=Article.objects.filter(status=True)
    serializer_class=ArticleSerializer
    def get_permissions(self):
        if self.action in ['list','create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsStaffOrReadOnly,IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

class UserViewSet(ModelViewSet):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=(IsSuperUserOrStaffReadOnly,)