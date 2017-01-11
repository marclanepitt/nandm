from __future__ import unicode_literals

from django.db import models

# Create your models here.
class timeevent(models.Model):
    title = models.CharField(max_length=30)
    pic = models.URLField(max_length=200, blank=True)
    description = models.TextField()
    side = models.BooleanField(default=False)
    event_date = models.DateField(auto_now = False)

    def __str__(self):
        return self.title
