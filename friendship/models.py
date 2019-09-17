from django.db import models


class Friendship(models.Model):
    first_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='first_user')
    second_user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='second_user')
    first_accepted = models.BooleanField(default=False)
    second_accepted = models.BooleanField(default=False)

    class Meta:
        ordering = ['id']

    def __str__(self):
        if self.first_accepted and self.second_accepted:
            return f"between {self.first_user} and {self.second_user}"
        elif not self.first_accepted and not self.second_accepted:
            return f"{self.second_accepted} and {self.first_user} are not friends"
        elif self.first_accepted and not self.second_accepted:
            return f"{self.first_user} follows {self.second_user}"
        else:
            return f"{self.second_accepted} follows {self.first_user}"
