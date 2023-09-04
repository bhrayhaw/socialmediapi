from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    GENDER_CHOICE = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )
    owner = models.ForeignKey(User, related_name='profile_data', on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=30, 
        choices=GENDER_CHOICE, 
        null=False, 
        blank=False)
    dob = models.DateField(default=None)
    phone = models.CharField(max_length=20)
    works_at = models.CharField(max_length=200, blank=True, null=True)
    studies_at = models.CharField(max_length=200, blank=True, null=True)
    profile_image = models.ImageField(upload_to="profile_image", blank=True, null=True)

    def __str__(self):
        return self.owner.username
