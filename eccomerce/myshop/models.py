from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=25,null=False)
    product_category=models.CharField(max_length=25)
    product_sub_category=models.CharField(max_length=15)
    product_desc=models.CharField(max_length=75,null=False)
    product_add_date=models.DateTimeField(auto_now_add=True)
    product_manufact_date=models.DateField()
    product_expiry_date=models.DateField()
    product_price=models.DecimalField(max_digits=25,decimal_places=2,null=False)
    product_manufacturer=models.ForeignKey(User,on_delete=CASCADE)
    product_piece_left=models.IntegerField()
    order_id=models.CharField(unique=True,max_length=100,null=True,blank=True)
    check_sum=models.CharField(max_length=100,null=True,blank=True)
    def save(self,*args,**kwargs):
        if self.order_id is None and self.product_manufact_date and self.id:
            self.order_id=self.product_manufact_date.strftime('ZAR%Y%m%dODR') + str(self.id)
        return super().save(*args,**kwargs)
    def __str__(self):
        return self.product_name
