from dataclasses import fields
from django import forms
from .models import UrlData

class UrlForm(forms.ModelForm):
    class Meta:
        model = UrlData
        fields = ['long_url']
        labels = {
            'long_url': 'URL:'
        }
        
