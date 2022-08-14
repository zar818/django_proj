from django.http.response import HttpResponseRedirect
from crudbase.models import User
from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'others/home.html')
def user_dash_board(request):
    if request.method=='POST':
        fm=ContactForm(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            pw=fm.cleaned_data['password']
            reg=User(name=nm,email=em,password=pw)
            reg.save()
            messages.success(request,'Your account has created successfully.')
            fm=ContactForm()
    else:
        fm=ContactForm() 
    regre=User.objects.all           
    return render(request,'others/dash_board.html',{'form':fm,'st':regre,})    
def delete(request,id):
    if request.method=='POST':
        pi=User(pk=id)
        pi.delete()
    return HttpResponseRedirect('/dashboard/')    
def update(request,id):
    if request.method=='POST':
        us=User.objects.get(pk=id)
        up=ContactForm(request.POST,instance=us)
        if up.is_valid():
            up.save() 
            messages.success(request,'Your account has been updated successfully.')
            us=User()
    else:
        us=User.objects.get(pk=id)
        up=ContactForm(request.POST,instance=us)
    return render(request,'others/update.html',{'sav':up})    


            