from __future__ import unicode_literals

from django.db import models

class Photo(models.Model):
    url = models.URLField(max_length=200)
    date_published = models.DateTimeField(auto_now_add=True)
