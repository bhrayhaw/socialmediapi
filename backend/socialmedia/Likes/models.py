from django.db import models
from post.models import Posts
# Create your models here.
class Likes(models.Model):
    posts = models.ForeignKey(Posts, related_name='likes', on_delete=models.CASCADE)
    like = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='like', default=None, blank=True, null=True)
    unlike = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='unlike', default=None, blank=True, null=True)

    def __str__(self):
        return self.posts.text