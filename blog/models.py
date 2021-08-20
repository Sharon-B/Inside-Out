from django.db import models
from django.contrib.auth.models import User


# Blog post model
class BlogPost(models.Model):

    class Meta:
        ordering = ['-created_on']

    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='blog_posts')
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(null=True, blank=True)
    body_text = models.TextField(default=None, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title
