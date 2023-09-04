from django.db import models
from post.models import Posts
# Create your models here.
class Follow(models.Model):
    owner = models.ForeignKey('auth.User', related_name='follow', on_delete=models.CASCADE)
    Follow = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='following', default=None, blank=True, null=True)
    Unfollow = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='unfollowing', default=None, blank=True, null=True)

    def __str__(self):
        return self.owner.username