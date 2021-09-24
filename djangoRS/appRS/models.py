from django.db import models

# Create your models here.

from django.db import models

class Image(models.Model):
    Id = models.IntegerField(auto_created=True, default=1, primary_key=True)
    Name = models.CharField(max_length=150)
    Extension = models.CharField(max_length=10)
    ZipCode = models.CharField(max_length=9,null=True)
    Address = models.CharField(max_length=150,null=True)
    Contents = models.TextField(null=True)