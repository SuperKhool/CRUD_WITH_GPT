from django.db import models

# Create your models here.

class Employ(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=200)
    profile_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    phone = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    def __str__(self):
        return self.name
    
    