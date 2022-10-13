# from unittes...t.ut......il import _MAX_LENGTH
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.db import models
# from django.db.models.fields import unique
from django.db.models import fields


class Thing(models.Model):
    name= models.CharField(max_length=30, unique=True, blank=False)
    description= models.TextField(max_length=120, blank=True)
    quantity= models.IntegerField(
        validators=[
            MaxLengthValidator(limit_value=100,message='Quantity cannot be greater than 100'),
            MinLengthValidator(limit_value=0, message='Quantity cannot be less than 0')
        ]
          
    )
