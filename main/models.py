from django.db import models

# Create your models here.

class Bus(models.Model): #모델명의 첫글자는 대문자로
    number = models.IntegerField(default=0)
    check = models.IntegerField(default=0)
