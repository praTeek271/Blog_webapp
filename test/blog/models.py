from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

class UserProfile(models.Model):
    user = models.CharField(max_length=200)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='./profile_pics/', blank=True)

    def get_profile_picture(self):
        return(mark_safe("<img src='{}' width='50px' height='50px' style='border-radius: 50%;' />".format(self.profile_picture.url)))
    get_profile_picture.short_description = 'Profile Picture'
    get_profile_picture.allow_tags = True

    def __str__(self):
        return(self.user)

class BlogPost(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'), 
        ('published', 'Published'))

    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
