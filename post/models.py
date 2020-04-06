from django.db import models
from django.core.files.storage import FileSystemStorage

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    contents = models.TextField()
    image = models.ImageField(storage=FileSystemStorage(location='assets/images/uploads'))
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
