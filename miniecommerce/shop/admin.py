from django.contrib import admin
from .models import Cart, CustomUser, Product, ProductInCart, Deal
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, AdminPasswordChangeForm
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.contrib.auth.admin import UserAdmin
# Register your models here.
class ProductInCartInline(admin.TabularInline):
    model=ProductInCart
class CartInLine(admin.TabularInline):
    model=Cart
class DealInline(admin.TabularInline):
    model=Deal.user.through


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets=(
        (None,{'fields': ('username','password')}),
        ('Personal Info',{'fields':('first_name','last_name','email','country')}),
        ('Permissions',{'fields':('is_superuser','is_staff',('is_active','is_verified'))}),
        ('Important Dates',{'fields':('date_joined','last_login')}),
        ('Advanced Options',{
            'classes':('collapse',),
            'fields':('groups','user_permissions'),
        }),
        ('Type',{'fields':('is_seller','is_customer')})
    )
    add_fieldsets=(
        (None,{
            'classes': ('wide',),
            'fields': ('username','first_name','last_name','email','password1','password2','is_seller','is_customer')
        }),
    )
    add_form=CustomUserCreationForm
    form=CustomUserChangeForm
    model=CustomUser
    list_display=['id','username','email','is_staff']
    list_filter=['is_staff','email']
    inlines=[
        CartInLine,DealInline
    ]
    search_fields=['username','email']

@admin.register(Product)    
class ProductAdmin(admin.ModelAdmin):
    list_display=['product_id','product_name','price',]

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display=['cart_id','created_on']
