from django.db import models
from users.models import CustomUser
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
