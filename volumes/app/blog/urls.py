from django.urls import path,include

from rest_framework import routers

from .views import ArticleViewSet,UserViewSet

app_name='api'

router = routers.SimpleRouter()
router.register('', ArticleViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('',include(router.urls))
]