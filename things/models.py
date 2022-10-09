from unittest.util import _MAX_LENGTH
from django.db import models

class Thing(models.Model):
    name= models.CharField(max_length=100)
    description= models.TextField()
    quantity= models.IntegerField()
