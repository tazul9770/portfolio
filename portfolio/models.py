from django.db import models
from cloudinary.models import CloudinaryField

class Project(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200)
    live_link = models.URLField(blank=True, null=True)
    github_frontend_link = models.URLField(blank=True, null=True)
    github_backend_link = models.URLField(blank=True, null=True)
    image = CloudinaryField('image')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class Skill(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()

class Contact(models.Model):
    email = models.EmailField()
    phone_number = models.CharField(max_length=11)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)