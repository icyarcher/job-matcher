from django.db import models
from django.contrib.auth.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title   

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cv = models.FileField(upload_to='cvs/')
    experience = models.TextField()
    education = models.TextField()
    preferred_location = models.CharField(max_length=200)
    def __str__(self):
        return self.user.username
