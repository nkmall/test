from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GEN_CHO=(
    (None, 'Sex:'),
    ('M', 'Male'),
    ('F', 'Female')
)

class User(AbstractUser):
    address=models.CharField(max_length=100)
    number=models.IntegerField(default="0512")
    gender=models.CharField(choices=GEN_CHO,max_length=1)