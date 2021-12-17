from django.shortcuts import redirect
from rest_framework.generics import ListAPIView, CreateAPIView
from django.views import View
from django.conf import settings
from .models import Link
from .serializer import LinkSerializer

class UrlShortenerApiView(ListAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer

class UrlShortenerCreateApiView(CreateAPIView):
    serializer_class = LinkSerializer

class Redirector(View):
    def get(self, request, *args, **kwargs):
        short: str = settings.HOST_URL + '/' + self.kwargs['short']
        redirect_url: str = Link.objects.filter(short=short).first().long

        return redirect(redirect_url)
