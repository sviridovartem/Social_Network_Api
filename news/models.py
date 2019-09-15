from django.db import models


class News(models.Model):
    group = models.ForeignKey('group.Group', on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True, default='')
    text = models.TextField()
    published_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ('published_at',)

    def __str__(self):
        return self.title
