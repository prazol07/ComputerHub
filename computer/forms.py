from dataclasses import field
from django import forms
from .models import *

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields ='__all__'

        
