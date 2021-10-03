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
    Latitude = models.DecimalField(max_digits=30, decimal_places=18, null=True); #위도
    Longitude = models.DecimalField(max_digits=30, decimal_places=18, null=True); #경도


class goodBad(models.Model):
    username = models.CharField(max_length=100)
    select1 = models.CharField(max_length=10)
    select2 = models.CharField(max_length=10)
    select3 = models.CharField(max_length=10)
    rec1 = models.CharField(max_length=10, default=None, null=True)
    rec2 = models.CharField(max_length=10, default=None, null=True)
    rec3 = models.CharField(max_length=10, default=None, null=True)
    eval = models.BooleanField(default=None, null=True)

