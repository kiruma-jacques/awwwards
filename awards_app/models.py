from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    avi=ImageField(manual_crop='')
    bio=models.CharField(max_length=240)
    phone=models.IntegerField(blank=True)
    email=models.EmailField()

class Project(models.Model):
    user=models.ForeignKey(User)
    profile=models.ForeignKey(Profile)
    title=models.CharField(max_length=150)
    landing=ImageField(manual_crop='')
    description=models.TextField()
