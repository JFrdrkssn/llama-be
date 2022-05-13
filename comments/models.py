from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    """
    Model for comments on the site.
    'owner' is the user who commented.
    'post' is the post the user commented on.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        """
        Order comment creation date in descending order, newest first.
        """
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.owner} commented: {self.content}'
