from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

# Create your models here.
class BaseUser(PermissionRequiredMixin,AbstractBaseUser):
    username=models.CharField(_('Username'),max_length=20,unique=True,blank=True)
    email=models.EmailField(_('Email'),unique=True,blank=False,null=False)
    first_name=models.CharField(_('First Name'),max_length=20,blank=False)
    last_name=models.CharField(_('Last Name'),max_length=20,blank=True)
    section=models.CharField(_('Section'),blank=True)
    teacher=models.BooleanField(_('Teacher'))
    student=models.BooleanField(_('Student'))
    address=models.CharField(_('Address'))
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
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    USERNAME_FIELD=['email']
    REQUIRED_FIELD=[]
    class Meta:
        abstract=True
    def __str__(self):
        return self.username   


class Teacher(models.Model):
    user=models.OneToOneField(BaseUser,on_delete=models.CASCADE)
    subject=models.CharField(_('subject'))
    teacher_ID=models.CharField(_('teacher id'),blank=False)
class Student(models.Model):
    user=models.OneToOneField(BaseUser,on_delete=models.CASCADE)   
    roll=models.IntegerField(_('roll')) 
    clas=models.CharField(_('class'))
    CHOICES=(
        ('UNITY','UNITY'),
        ('FAITH','FAITH'),
        ('DISCIPLINE','DISCIPLINE'),
        ('TOLERANCE','TOLERANCE')
    )
    group=models.CharField(_('group'),choices=CHOICES)
