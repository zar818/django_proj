from re import T
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django_countries.fields import CountryField
from django.utils import timezone
from .manager import CustomManager
# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    age=models.IntegerField(_('age'),null=True, blank=True)
    country=CountryField()
    address=models.CharField(max_length=70,null=True,blank=True)
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    is_superuser=models.BooleanField(
        _('Superuser'),
        default=False,
        help_text=_(
            'Designates whether this user have administrative authority or not'
            
        )
    )
    is_verified=models.BooleanField(
        _('verfied'),
        default=False,
        help_text=_(
            'Stats whether the account is verified or Not'
            
        )
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_login = models.DateTimeField(_('date joined'), default=timezone.now)
    is_seller=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=True)
    

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomManager()
    
    def __str__(self):
        return self.username
class Author(models.Model):
    title=models.CharField()
# class Comments(models.Model):
#     pass
# class add_to_cart(models.Model):
#     pass   
# class Order(models.Model):
#     pass    