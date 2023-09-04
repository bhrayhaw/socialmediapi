# #Model for Groups and GroupMembers
# from django.db import models

# # Create your models here.
# class UserGroups(models.Model):
#     name = models.CharField(max_length=50)
#     description = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return self.name
    
# class GroupMembers(models.Model):
#     group = models.ForeignKey(UserGroups, on_delete=models.CASCADE)
#     member = models.ForeignKey('user_registration.User', on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return f"{self.member} is member of {self.group}"
    
#     class Meta:
#         unique_together = ('group', 'member')

