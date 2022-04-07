from django.contrib.auth.models import User
from django.contrib.auth.forms import SetPasswordForm, UserChangeForm,UserCreationForm,UsernameField,PasswordChangeForm
from django.contrib.auth import password_validation
from django.utils.translation import gettext_lazy as _ 
from .models import Article
from django import forms

class AddArticle(forms.ModelForm):
    class Meta:
        model=Article
        fields=['title','body']
class SignUpForm(UserCreationForm):
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
        help_text=_("Enter the same password as before, for verification."),
    )
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        widgets={
            'username':forms.TextInput(attrs={
               'class':'form-control', 
            }),
            'first_name':forms.TextInput(attrs={
               'class':'form-control', 
            }),
            'last_name':forms.TextInput(attrs={
               'class':'form-control', 
            }),
            'email':forms.EmailInput(attrs={
               'class':'form-control', 
            }),
        }
class PasswordFormWithOldPassword(PasswordChangeForm):
    new_password1 = forms.CharField(
        label=_("New password"),
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=_("New password(Again)"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password','class':'form-control'}),
    )
    class Meta:
        model=User
        fields='__all__'
        widgets={
            'old_password':forms.PasswordInput(attrs={
                'auto-complete':'current-password','autofocus':True,'class':'form-control'
            })
        }
        labels={
            'old_password':'Current Password'
        }
class PasswordChangeWithoutOld(SetPasswordForm):
    class Meta:
        model=User
        fields=['new_password1','new_password2']  
        widgets={
            'new_password1':forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),
            'new_password1':forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'})
        }  
        labels={
            'new_password1':'New Password',
            'new_password2':'Password(Again)'
        }    
class EditUserForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','last_login','date_joined','is_active']
class EditAdminForm(UserChangeForm):
    class Meta:
        model=User
        fields='__all__'

