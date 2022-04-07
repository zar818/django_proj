from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from muslimapp.models import Article
from django.contrib.auth.models import Group
from django.http.response import HttpResponseRedirect
from muslimapp.forms import EditAdminForm, EditUserForm, SignUpForm, AddArticle, PasswordChangeWithoutOld, PasswordFormWithOldPassword
from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import messages
# Create your views here.
def home(request):
    pass

# class IdCreationForm(View):
#     def get(self,request):
#         form=SignUpForm()
#         context={
#             'form':form,
#         }
#         return render(request,'muslimapp/all/signup.html',context)
#     def post(self,request):
#         form=SignUpForm(request.POST)
#         context={
#             'form':form,
#         }
#         return render(request,'muslimapp/all/signup.html',context)

def signup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=SignUpForm(request.POST)
            if form.is_valid():
                messages.success(request,'Your account has been created successfully! ')
                save_user=form.save()
                group=Group.objects.get(name='Common')
                save_user.groups.add(group)
 
        else:
            form=SignUpForm()
        context={
            'form':form,
        }
        return render(request,'muslimapp/all/signup.html',context)
    else:
        return HttpResponseRedirect('/profile/')
def article(request):
    article=Article.objects.all()
    return render(request,'muslimapp/all/article.html',{'articles':article})
def password_wo_old_change(request):
    if request.method=='POST':
        form=PasswordChangeWithoutOld(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Password has been successfully!')
    else:
        form=PasswordChangeWithoutOld()
    context={
        'form':form,
    }
    return render(request,'muslimapp/all/passwordch.html',context)
def password_old(request):
    if request.method=='POST':
        form=PasswordFormWithOldPassword(user=request.user,data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your Password has been successfully!')
    else:
        form=PasswordChangeWithoutOld()
    context={
        'form':form,
    }
    return render(request,'muslimapp/all/passwordch.html',context)
def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request=request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,'You have logged in successfully.')
    else:
        form=AuthenticationForm()
    context={
        'form':form,
    }
    return render(request,'muslimapp/all/log.html',context)
def user_logout(request):
    if request.user.is_authenticated:
     logout(request)
     messages.success(request,'You have logged out successfully.')
    return HttpResponseRedirect('/login/')
def update_article(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            form=AddArticle(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,'Your article has been updated.')
        else:
            form=AddArticle()
        context={
            'form':form
        }
        return render(request,'muslimapp/all/update_article.html',context)
    else:
        return HttpResponseRedirect('/login/')
    