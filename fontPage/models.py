from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField

class fontpage(models.Model):
    name = models.TextField(max_length=50)
    title = models.CharField(max_length=100)
    description = HTMLField()
    # image = models.ImageField(upload_to='images/')
    
    new_slug = AutoSlugField(populate_from='name', unique=True, null=True, default=None)
# Create your models here.
