from django.db import models
from tinymce.models import HTMLField

class contactNum(models.Model):
    firstname = models.TextField(max_length=50)
    lestname = models.TextField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    number = models.CharField(max_length=12)
    description = HTMLField()
    con_image = models.ImageField(upload_to='images/', max_length=250, default=None, null=True, blank=True)  
# Create your models here.
