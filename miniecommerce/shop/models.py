from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from .manager import CartManager, CustomUserManager
from django_countries.fields import CountryField

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        _('username'),
        max_length=150,
        unique=True,
        help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        validators=[username_validator],
        error_messages={
            'unique':("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_('first name'), max_length=150, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    country=CountryField()
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text=(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField( default=timezone.now)
    is_verified=models.BooleanField(
        _('Verified'),
        default=False,
        help_text=_(
            'States Whether Account is verified through Email or Not.'
        ))
    is_seller=models.BooleanField(
        _('Seller'),
        default=False,
        help_text=_(
            'States Whether is Account holder is Seller or Not '
        ))
    is_customer=models.BooleanField(
        _('Customer'),
        default=True,
        help_text=_(
            'States Whether is Account holder is Customer or Not'
        ))

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    def __str__(self):
        return self.username
class Product(models.Model):
    product_id=models.AutoField(primary_key=True)  
    product_name=models.CharField(max_length=24)
    price=models.IntegerField()
    stock=models.IntegerField()
    discount=models.CharField(max_length=10,blank=True) 
    @classmethod
    def updateprice(cls,product_id,price):
        product=cls.objects.filter(product_id=product_id)
        product=product.first()
        product.price=price
        product.save()
        return product
    @classmethod
    def create(cls,product_name,price,stock,discount=None):
        product=Product(product_name=product_name,price=price,stock=stock,discount=discount)
        product.save()
        return product
    def __str__(self):
        return self.product_name 
class Cart(models.Model):
    cart_id=models.AutoField(primary_key=True)
    user=models.OneToOneField(CustomUser,on_delete=models.CASCADE)  
    created_on=models.DateTimeField(default=timezone.now)   
    objects= CartManager()
class ProductInCart(models.Model):
    class Meta:
        unique_together=('cart','product')
    product_in_cart_id=models.AutoField(primary_key=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    quantity=models.IntegerField()
class Order(models.Model):
    CHOICES=(
        (1,'Not Packed'),
        (2,'Ready For Shipment'),
        (3,'Shipped'),
        (4,'Delivered'),
    )
    status=models.IntegerField(choices=CHOICES,default=1)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
class Deal(models.Model):
    user=models.ManyToManyField(CustomUser)
    deal_name=models.CharField(max_length=145)
    
    
    
