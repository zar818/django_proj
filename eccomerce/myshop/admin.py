from myshop.models import Product
from django.contrib import admin

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','product_name','product_desc','product_manufacturer','product_piece_left','product_add_date','product_price']