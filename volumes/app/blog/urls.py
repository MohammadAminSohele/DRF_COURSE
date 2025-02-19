from django.urls import path,include

from rest_framework import routers

from .views import ArticleViewSet,UserViewSet,AuthorRetrive

app_name='api'

router = routers.SimpleRouter()
router.register('articles', ArticleViewSet,basename="articles")
router.register('users', UserViewSet,basename="users")

urlpatterns = [
    path('',include(router.urls)),
    path('authors/<int:pk>/',AuthorRetrive.as_view(),name='AuthorRetrive'),
]