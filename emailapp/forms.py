from django import forms

class mailForm(forms.Form):
    to=forms.EmailField()
    subject=forms.CharField(max_length=100)
    message=forms.CharField(max_length=100)
