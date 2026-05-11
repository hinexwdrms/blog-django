from django.db import models
from django.contrib.auth.models import User ## Django's built-in User model (handles auth)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # many posts can belong to one user, delete posts if user is deleted
    created_at = models.DateTimeField(auto_now_add=True)