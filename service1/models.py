from django.db import models

class Book(models.Model):
    Book_icon = models.CharField(max_length=100)
    Book_title = models.CharField(max_length=100)
    Book_des = models.TextField()
# Create your models here.
