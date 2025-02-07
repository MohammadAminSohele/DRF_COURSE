from django.urls import path

from .import views

app_name='api'

urlpatterns = [
    path('',views.ArticleList.as_view(),name='ArticleList'),
    path('<int:pk>',views.ArticleDetail.as_view(),name='ArticleDetail'),

    path('user/',views.UserList.as_view(),name='UserList'),
    path('user/<int:pk>',views.UserDetail.as_view(),name='UserDetail'),
]