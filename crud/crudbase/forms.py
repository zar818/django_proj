from django import forms
from django.forms import widgets
from .models import User
class ContactForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','password','email']
        widgets={
            'name':forms.TextInput(attrs={'class':'control-form'}),
            'email':forms.EmailInput(attrs={'class':'control-form'}),
            'password':forms.PasswordInput(render_value=True, attrs={'class':'control-form'}),
        }