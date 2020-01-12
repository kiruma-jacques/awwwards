from django import forms
from .models import Profile, Project

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class ProjectUpload(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['user','profile']
