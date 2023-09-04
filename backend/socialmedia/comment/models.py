from django.db import models
from post.models import Posts
# Create your models here.
class Comments(models.Model):
    owner = models.ForeignKey('auth.User', related_name='comments', on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, related_name='comments', on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000, blank=True)
    comment_image = models.ImageField(upload_to='comments/images/', blank=True)
    comment_video = models.FileField(upload_to='comments/videos/', blank=True)
    comment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.owner.username} commented {self.comment} on {self.post.text}"
