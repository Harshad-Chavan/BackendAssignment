import django.forms
from django import forms


class Login(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(max_length=16, widget=forms.PasswordInput)
