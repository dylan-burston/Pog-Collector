from django.db import models

# Create your models here.
class Pog(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
