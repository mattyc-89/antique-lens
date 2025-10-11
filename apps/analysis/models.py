from django.db import models
from django.conf import settings

# Create your models here.

class Antique(models.Model):
    title = models.CharField(max_length=200)
    year = models.IntegerField(max_length=4)
    description = models.TextField(blank=True, null=True)

    # The image file will be uploaded to MEDIA_ROOT/antique_images with a date-based subdirectory
    # e.g., MEDIA_ROOT/antique_images/2025/09/16/
    image = models.ImageField(upload_to='antique_images/%Y/%m/%d/', null=False, blank=False) 

    # Connect to new user model in settings.py via settings.AUTH_USER_MODEL
    user = settings.AUTH_USER_MODEL
    user = models.ForeignKey(user, on_delete=models.CASCADE, null=True, blank=True) 
    uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title