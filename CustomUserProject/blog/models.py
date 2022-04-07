from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.validators import UnicodeUsernameValidator
from django_countries.fields import CountryField
from .manager import CustomManager
# Create your models here.

class CustomUser(AbstractBaseUser,PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique': _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), blank=True,unique=True)
    age=models.IntegerField(_('age'),null=True, blank=True)
    country=CountryField()
    address=models.CharField(max_length=70)
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
    is_verified=models.BooleanField(
        _('verfied'),
        default=False,
        help_text=_(
            'Stats whether the account is verified or Not'
            
        )
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    last_login = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = CustomManager()

    

    EMAIL_FIELD='email'
    USERNAME_FIELD='username'
    def __str__(self):
        return self.email
class product(models.Model):
    product_id=models.AutoField(unique=True, primary_key=True)        