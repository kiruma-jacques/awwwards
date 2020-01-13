from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField
from django.core.validators import MaxValueValidator,MinValueValidator
# Create your models here.
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    avi=ImageField(manual_crop='')
    bio=models.CharField(max_length=240)
    phone=models.IntegerField(blank=True)
    email=models.EmailField()

class Project(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='project')
    title=models.CharField(max_length=150)
    landing=ImageField(manual_crop='')
    description=models.TextField()
    live_site=models.URLField(max_length=299)

class Review(models.Model):
    project=models.ForeignKey(Project,on_delete=models.CASCADE,related_name='review')
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='review')
    comment=models.TextField()
    design=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    useability=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    content=models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    
