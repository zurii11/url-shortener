from django.db import models
from django.conf import settings
from random import choices
from string import ascii_letters

class Link(models.Model):
    long: str = models.URLField(max_length=250)
    short: str = models.URLField(blank=True, null=True)
    customURL: str = models.CharField(blank=True, null=True, max_length=9)

    def shorten(self) -> str:
        while True:
            unique_key: str = ''.join(choices(ascii_letters, k=9))
            new: str = settings.HOST_URL + '/' + unique_key

            if not Link.objects.filter(short=new).exists():
                break

        return new

    def custom(self) -> str:
        if not Link.objects.filter(short=self.customURL).exists():
            if len(self.customURL) <= 9:
                new: str = settings.HOST_URL + '/' + self.customURL
                return new
            else:
                raise Exception("Key should be no longer than 9 characters!")

    def save(self, *args, **kwargs):
        if len(self.customURL) > 0:
            self.short = self.custom()
        else:
            self.short = self.shorten()

        super().save(*args, **kwargs)
