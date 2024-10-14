from django.db import models

# Create your models here.
class upload(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    description = models.CharField(max_length=500)
    profile = models.ImageField(upload_to= 'profiles/')