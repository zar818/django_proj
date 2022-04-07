from django.contrib.auth.models import User
from .models import Post, Article, ArtWork
from django import forms
from django.contrib.auth.forms import UserCreationForm
class ArticleForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=['article_title','main_article']
class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title','text','image','user']
class ArtworkForm(forms.ModelForm):
    class Meta:
        model=ArtWork
        fields=['art','art_desc']
class SignupForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        widgets={
            'username':forms.TextInput(attrs={
                'class':'control-form'
            }),
            'first_name':forms.TextInput(attrs={
                'class':'control-form'
            }),
            'last_name':forms.TextInput(attrs={
                'class':'control-form'
            }),
            'email':forms.EmailInput(attrs={
                'class':'control-form'
            }),
        }