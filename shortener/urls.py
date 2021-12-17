from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from api.views import UrlShortenerApiView, UrlShortenerCreateApiView, Redirector

urlpatterns = [
    path('api/', UrlShortenerApiView.as_view(), name='everything'),
    path('api/create/', UrlShortenerCreateApiView.as_view(), name='create'),
    path('<str:short>/', Redirector.as_view(), name='redirector')
]
