from django.db import models
from django.contrib.auth.models import User, AbstractUser
# Create your models here.


class Income(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
class Expense(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)