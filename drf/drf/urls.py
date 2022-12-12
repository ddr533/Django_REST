from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView

from women.views import *


# """Роутеры для маршрутов для viewset"""
#
# router = routers.SimpleRouter()
# router.register(r'women', WomenViewSet, basename='women')    #basename - префикс к именам маршрутов, по умолчанию равен имени модели, обязателен, если во вьюсете не определен атрибут queryset.
# print(router.urls)
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/', include(router.urls)),   # http://127.0.0.1:8000/api/v1/women/
# ]


# """Маршруты для viewsets"""
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list'})),               #ключ - тип запроса, значение - метод класса для обработки
#     path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
# ]



"""Маршруты для generics"""

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/v1/womenlist/', WomenAPIView.as_view()),
    # path('api/v1/womenlist/<int:pk>/', WomenAPIView.as_view()),
    path('api/v1/womenlist/', WomenAPIList.as_view()),
    path('api/v1/womenlist/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/womendetail/<int:pk>/', WomenAPIDetailView.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenAPIDestroy.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),                   #для аутентификации по сессиям
    path('api/v1/auth/', include('djoser.urls')),                               #для аутентификации по токенам Djoser
    re_path(r'^auth/', include('djoser.urls.authtoken')),                       #для аутентификации по токенам Djoser
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'), #для аутентификации по токенам JWT
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),#для обновления токена accsess JWT
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),   #для верификации токена JWT
]
