from django.db import models


class Group(models.Model):
    author = models.CharField(max_length=100, blank=True, default='',)
    name = models.CharField(max_length=100, blank=True, default='', unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
