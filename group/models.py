from django.db import models


class Group(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='author')
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ('name',)

    def save(self, *args, **kwargs):
        super(Group, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
