from django.db import models


# Create your models here.
class Posts(models.Model):
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)   
    text = models.TextField(max_length=1000, blank=True)
    image = models.ImageField(upload_to='posts/images/', blank=True)
    video = models.FileField(upload_to='posts/videos/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.owner.username} posted {self.text}"
    
