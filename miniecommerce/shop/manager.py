from django.contrib.auth.models import BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    '''
    Custom Manager where email is required rather than username
    '''
    def create_user(self,email,password,**extrafields):
        if email is None:
            raise ValueError('Email is Required.')
        email=self.normalize_email(email)
        user=self.model(email=email,**extrafields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self,email,password,**extrafields):
        extrafields.setdefault('is_active',True)
        extrafields.setdefault('is_superuser',True)
        extrafields.setdefault('is_staff',True)
        if extrafields.get('is_staff') is False:
            raise ValueError('Superuser must be staff')
        if extrafields.get('is_superuser') is False:
            raise ValueError('superuser states must be True for Super User')
        return self.create_user(email=email,password=password,**extrafields)
class CartManager(models.Manager):
    def create_cart(self,user):
        cart=self.create(user=user)
        cart.save()
        return cart
