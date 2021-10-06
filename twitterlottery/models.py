from django.db import models

# Create your models here.
class TwitterForm(models.Model):
    link = models.CharField(max_length = 100)
    countPeople = models.CharField(max_length=20)

