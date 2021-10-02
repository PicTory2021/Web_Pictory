import django
from django.db import models

# Create your models here.

from django.db import models
from datetime import datetime

from django.utils import timezone


class UserDB(models.Model):
    UserId = models.IntegerField(auto_created=True, default=1, primary_key=True)
    UserName = models.CharField(max_length=100)

class Image(models.Model):
    Id = models.IntegerField(auto_created=True, default=1, primary_key=True)
    Name = models.CharField(max_length=150)
    Extension = models.CharField(max_length=10)
    ZipCode = models.CharField(max_length=9,null=True)
    Address = models.CharField(max_length=150,null=True)
    Contents = models.TextField(null=True)
    Latitude = models.DecimalField(max_digits=30, decimal_places=18, null=True); #위도
    Longitude = models.DecimalField(max_digits=30, decimal_places=18, null=True); #경도

class DetailClick(models.Model): #결과 중 자세히보기를 선택한 관광지 DB
    Id = models.AutoField(primary_key=True)
    UserId = models.IntegerField()
    UserName = models.CharField(max_length=100)
    SelectImage = models.CharField(max_length=150)
    clickOpenDate = models.DateTimeField(default=django.utils.timezone.now)
    stayTime = models.FloatField(default=0)

