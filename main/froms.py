from django import forms

class NewList(forms.Form):
    name = forms.CharField(max_length=150, label="Name")
    check = forms.BooleanField(required=False)
    
