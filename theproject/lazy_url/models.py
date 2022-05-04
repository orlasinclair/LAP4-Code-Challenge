from django.db import models

class ShortUrls(models.Model):
    long_url = models.URLField(max_length=200)
    short_url = models.CharFiedl(max_length=15, unique=True)

    def __str__(self):
        return f'{self.long_url} becomes {self.short_url}'
