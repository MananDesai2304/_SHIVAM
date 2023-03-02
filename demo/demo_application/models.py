from django.db import models

# Create your models here.

class common_user(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)