from django import forms
from .models import Profile, Project

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=Profile
        exclude=['user']

class ProjectUploadForm(forms.ModelForm):
    class Meta:
        model=Project
        exclude=['user']
