from django import forms
from .models import CRUD


class CRUDFORM(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "name"
    }))
    age= forms.CharField(widget=forms.TextInput(attrs={
        'type': "number",
        "class": "form-control",
        "placeholder": "age"
    }))
    
    level = forms.CharField(widget=forms.TextInput(attrs={
        "class": "form-control",
        "placeholder": "level"
    }))
    class Meta:
        model = CRUD
        fields = [
            'name', 'age','level'
        ]

    