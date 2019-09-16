from django.db import models


class News(models.Model):
    group = models.ForeignKey('group.Group', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('published_at',)

    def __str__(self):
        return self.title
