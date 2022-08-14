from django import forms
from .models import CustomUser
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.db import models
class SignForm(UserCreationForm):
    password1=forms.SlugField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))
    password2=forms.SlugField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm password'}))
    class Meta:
        model=CustomUser
        fields=['username','email']
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Enter username'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter email address'})
        }
class LoginForm(AuthenticationForm):
    username=forms.EmailField(widget=forms.EmailInput(attrs={'placeholder':'Enter email address'}))
    password=forms.SlugField(widget=forms.PasswordInput(attrs={'placeholder':'Enter password'}))
    class Meta:
        model=CustomUser
        fields=['email','password']
              