from django.db import models

class User(models.Model):
  name = models.CharField(max_length=50, null=False)
  nick = models.CharField(max_length=30, null=False)
  avatar = models.CharField(max_length=100, null=False)