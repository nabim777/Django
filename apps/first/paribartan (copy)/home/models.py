from django.db import models
from django import forms
# Create your models here.
class Register(forms.Form):
    name = forms.CharField(max_length=122)
    geeks_field = forms.IntegerField(max_length = 122)
    address = forms.CharField(max_length=122)
    email = forms.EmailField(max_length=122)
    password1 = forms.CharField(widget = forms.PasswordInput())
    password2 = forms.CharField(widget = forms.PasswordInput())