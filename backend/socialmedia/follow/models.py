# from django.db import models

# # Create your models here.
# # Model for UserFollowers, UserFollowing 
# class UserFollowing(models.Model):
#     user = models.ForeignKey('user_registration.User', on_delete=models.CASCADE)
#     following = models.ForeignKey('user_registration.User', on_delete=models.CASCADE, related_name='following')
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.user} following {self.following}"
    
#     class Meta:
#         unique_together = ('user', 'following')


# class UserFollowers(models.Model):
#     user = models.ForeignKey('user_registration.User', on_delete=models.CASCADE)
#     follower = models.ForeignKey('user_registration.User', on_delete=models.CASCADE, related_name='follower')
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.user} followed by {self.follower}"
    
#     class Meta:
#         unique_together = ('user', 'follower')

