from django.db import models


# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=16, null=False, unique=True)
    password = models.CharField(max_length=32, null=False)
    email = models.EmailField(max_length=32, null=False, unique=True)
