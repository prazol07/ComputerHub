from dataclasses import field
from django import forms
from .models import *

class ComputerForm(forms.ModelForm):
    class Meta:
        model = Computer
        fields =['computer_code', 'computer', 'computer_specification', 'brand', 'quantity', 'unit_rate']
        

        
