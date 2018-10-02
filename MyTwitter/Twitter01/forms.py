from urllib import request

from django import forms
from django.contrib.auth.models import User

from .models import Tweet


class UserForm(forms.ModelForm):
   class Meta:
       model = User
       fields = ("username",  "first_name", "last_name", "email")

   password = forms.CharField(label='Password', widget=forms.PasswordInput)
   #confirm_password = forms.CharField(label='Confirm password', widget=forms.PasswordInput)


class LoginForm(forms.Form):
    login = forms.CharField(label='login')
    password = forms.CharField(label='password', widget=forms.PasswordInput)


class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        exclude = ['dependence']

