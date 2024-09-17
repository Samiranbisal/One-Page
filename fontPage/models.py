from django.db import models
from tinymce.models import HTMLField

class fontpage(models.Model):
    name = models.TextField(max_length=50)
    title = models.CharField(max_length=100)
    description = HTMLField()
    # image = models.ImageField(upload_to='images/')
# Create your models here.
