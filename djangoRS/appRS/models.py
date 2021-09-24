from django.db import models

# Create your models here.

from django.db import models

class Image(models.Model):
    Name = models.CharField(max_length=150, primary_key=True)
    Extension = models.CharField(max_length=10)
    ZipCode = models.CharField(max_length=9,null=True)
    Address = models.CharField(max_length=150,null=True)
    Contents = models.TextField(null=True)