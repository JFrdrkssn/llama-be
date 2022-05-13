from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    """
    Model for followers on the site.
    A 'owner' is a User who follows an other user.
    'followed' is a User who is followed by 'owner'.
    """
    owner = models.ForeignKey(
        User, related_name='following', on_delete=models.CASCADE
    )
    followed = models.ForeignKey(
        User, related_name='followed', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        'unique_together' prevents users from
        following other users more than once.
        """
        ordering = ['-created_at']
        unique_together = ['owner', 'followed']

    def __str__(self):
        return f'{self.owner} {self.followed}'
