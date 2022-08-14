from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.forms import PasswordChangeForm,AuthenticationForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.models import User,Group
from .forms import LoginForm, PasswordForm, PostForm, SignupForm,EditAdminProfile,EditProfile
from django.contrib import messages
from .models import Post

# Create your views here.
def home(request):
    if request.user.is_authenticated:
        postm=Post.objects.all()              
        
    else:
        postm=None
    context_dash={
        'fm':request.user,
        'pm':postm,
        }    
    return render(request,'all/home.html',context_dash)
def about(request):
    return render(request,'all/about.html')
def contact(request):
    return render(request,'all/contact.html')
def issues(request):
    if request.user.is_authenticated:
        postm=Post.objects.all()              
        context_dash={
        'fm':request.user,
        'pm':postm,
        }
        return render(request,'all/issues.html',context_dash)
    else:
        return HttpResponseRedirect('/login/') 
def signingup(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            form=SignupForm(request.POST)
            if form.is_valid():
                messages.success(request,'Your account has been created successfully.')
                saving_user=form.save()
                group=Group.objects.get(name='Common')
                saving_user.groups.add(group)
        else:
            form=SignupForm()
        context_sign={
        'form':form,
        }   
        return render(request,'all/signup.html',context_sign)
    else:
        return HttpResponseRedirect('/dashboard/')       
    
def loggingin(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            frm=LoginForm(request=request,data=request.POST)
            if frm.is_valid():
                fname=frm.cleaned_data['username']
                fpass=frm.cleaned_data['password']
                yougovi=authenticate(username=fname,password=fpass)
                if yougovi is not None:
                    login(request,yougovi)
                    messages.success(request,'You have been logged in.')
                    return HttpResponseRedirect('/dashboard/')
        else:
            frm=LoginForm 
        context_logg={
        'form':frm,
        }
        return render(request,'all/login.html',context_logg)
    else:
        return HttpResponseRedirect('/dashboard/') 
def dashboard(request,):
    if request.user.is_authenticated:
        pm=Post.objects.all()              
        context_dash={
        'fm':request.user,
        'pm':pm,
        }
        return render(request,'all/dashboard.html',context_dash)
    else:
        return HttpResponseRedirect('/login/')                         
def addpost(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            postform=PostForm(request.POST,instance=request.user)
            if postform.is_valid():
                postform.save()
                messages.success(request,'Your post has been uploaded.')
                return HttpResponseRedirect('/dashboard/')
        else:
            postform=PostForm()        
    return render(request,'all/addpost.html',{'pf':postform}) 
def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi=Post.objects.get(pk=id)
            posteditform=PostForm(request.POST,instance=pi)
            if posteditform.is_valid():
                posteditform.save()
                messages.success(request,'Your post has been updated successfully.')
                return HttpResponseRedirect('/issues/')
        else:
            pi=Post.objects.get(pk=id)
            posteditform=PostForm(instance=pi)
        contextupdate={
            'posteditform':posteditform,
        }    
        return render(request,'all/update.html',contextupdate)    
    else:
        return HttpResponseRedirect('/login/')
def deletepost(request,id):
    if request.user.is_authenticated:
        pi=Post(pk=id)
        pi.delete()
        messages.success(request,'Post has been deleted')
    return HttpResponseRedirect('/dashboard/')       
def editprofile(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            if request.user.is_superuser:
                form=EditAdminProfile(request.POST,instance=request.user)
                if form.is_valid():
                    form.save()
                    messages.success(request,'Your profile has been updated successfully.')
            else:
                form=EditProfile(request.POST,instance=request.user)    
                if form.is_valid():
                    form.save()
                    messages.success(request,'Your profile has been updated successfully.') 
        else:
            if request.user.is_superuser:
                form=EditAdminProfile(instance=request.user)
            else:
                form=EditProfile(instance=request.user)                
        context_dash={
        'form':form,
        }
        return render(request,'all/profile.html',context_dash)
    else:
        return HttpResponseRedirect('/login/')              
    
def ch_password(request):
    if request.method=='POST':
        frm=PasswordForm(user=request.user,data=request.POST)
        if frm.is_valid():
            frm.save()
            update_session_auth_hash(request,frm.user)
            messages.success(request,'Your password changed successfully.')
    else:
        frm=PasswordForm(user=request.user) 
               
    return render(request,'all/change.html',{'fm':frm})
def loggingout(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'You have been logged out successfully.')  
    return HttpResponseRedirect('/login/')
