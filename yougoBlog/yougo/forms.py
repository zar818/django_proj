from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm,UserChangeForm,UsernameField
from django.contrib.auth.models import User
from django.forms import fields
from django.utils.translation import gettext, gettext_lazy as _
from .models import Post

class SignupForm(UserCreationForm):
    password1=forms.CharField(max_length=28,widget=forms.PasswordInput(attrs={'placeholder':'Enter password here','class':'form-control'}),label='Password')
    password2=forms.CharField(max_length=28,widget=forms.PasswordInput(attrs={'placeholder':'Enter password here','class':'form-control'}),label='Confirm password')
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        label={
            'email':'Email',
        }
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Enter your name here.', 'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'placeholder':'Enter your first name here.','class':'form-control'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Enter your last name here.','class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter your email here.','class':'form-control'}),
        }
class EditProfile(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email',] 
        labels={
            'email':'Email',

        }
        widgets={
            'username':forms.TextInput(attrs={'placeholder':'Enter your name here.', 'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'placeholder':'Enter your first name here.','class':'form-control'}),
            'last_name':forms.TextInput(attrs={'placeholder':'Enter your last name here.','class':'form-control'}),
            'email':forms.EmailInput(attrs={'placeholder':'Enter your email here.','class':'form-control'}),
        }
class EditAdminProfile(UserChangeForm):
    class Meta:
        model=User
        fields='__all__'   
        labels={
            'email':'Email',

        }            
class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={'autofocus': True,'class':'form-control'}))
    password = forms.CharField(label=_("Password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'current-password','class':'form-control'}),) 
    class Meta:
        fields=['username','password']
class PostForm(forms.ModelForm):
    media=forms.FileField(required=None)
    class Meta:
        model = Post
        fields = ['title','media','body'] 
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            }
class PasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label=_("Old password"),strip=False,widget=forms.PasswordInput(attrs={'autocomplete': 'current-password', 'autofocus': True,'class':'forms-control'}),
    )
    '''A form that lets user to change their password by entering old password'''
    class Meta:
        fields='__all__'