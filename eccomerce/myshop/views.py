from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Product
# Create your views here.
def home(request):
    return render(request,'all/home.html')
def service(request):
    category=Product.objects.all().filter('product_category')
    sub_category=Product.objects.all().filter('product_sub_category')
    context={
        'cat':category,
        'sub':sub_category,
    }
    return render(request,'all/services.html',context)
def contact(request):
    return render(request,'all/contact.html')
def about(request):
    return render(request,'all/about.html')
class ProductShow(DetailView):
    model=Product
    template_name='all/product.html'
    context_object_name='product'
