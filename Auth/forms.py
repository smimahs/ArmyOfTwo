from django import forms
from django.forms import ModelForm
from Auth.models import Clients

class SignUpForm(forms.Form):
    name=forms.CharField(max_length=150)
    email=forms.CharField(max_length=150)
    password=forms.CharField(max_length=20)
    cpassword=forms.CharField(max_length=20)

class SignInForm(forms.Form):   
    email=forms.CharField(max_length=150)
    password=forms.CharField(max_length=20)
