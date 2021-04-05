from django import forms
from .models import ResumeData

class uploadForm(forms.Form):
    file = forms.FileField()