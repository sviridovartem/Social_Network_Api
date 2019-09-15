from django.db import models


class Subscription(models.Model):
    group = models.ForeignKey('group.Group', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return f"User {self.user} subscribed to {self.group}"
