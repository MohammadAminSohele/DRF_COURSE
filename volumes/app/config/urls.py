"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from .import settings

from django.conf.urls.static import static

# from dj_rest_auth.views import PasswordResetConfirmView
from rest_framework_simplejwt import views as jwt_views
# from blog.views import RevokeToken

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns+=[
    path('api/',include('blog.urls')),
]

urlpatterns+=[
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/rest-auth/', include('dj_rest_auth.urls')),
    # path('api/rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    # path('api/rest-auth/password/reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('api/token-auth/', obtain_auth_token),
    # path('api/revoke/', RevokeToken.as_view()),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)