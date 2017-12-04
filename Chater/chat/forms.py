from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import authenticate

class UserForms(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=200)
    confirm_password = forms.CharField()






