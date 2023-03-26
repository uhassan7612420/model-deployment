from django import forms

class Form(forms.Form):
    title = forms.CharField(max_length=50)
    file  = forms.FileField()