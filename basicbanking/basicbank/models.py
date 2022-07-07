from tkinter.tix import Tree
from django.db import models
from django.dispatch import receiver

# Create your models here.
class Users(models.Model):
    accno = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=100, null=True)
    accbal = models.IntegerField()

class Transfer(models.Model):
    sender = models.CharField(max_length=100, null=True)
    amount = models.IntegerField(default=0)
    receiver = models.CharField(max_length=100, null=True)
    datetrans = models.DateTimeField(auto_now=True)