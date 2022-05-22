from django.db import models


class Category(models.Model):
    """
    Model for categories on the site.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=55)

    class Meta:
        """
        Order category creation date in descending order, newest first.
        """
        ordering = ['-created_at']

    def __str__(self):
        return f'Category: {self.category}'
