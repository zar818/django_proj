from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

from blog.models import CustomUser
from blog.forms import LoginForm, SignForm
# Create your views here.
def home(request):
    return render(request,'misc/home.html')
def about(request):
    return render(request,'misc/about.html')    
def user_sign(request):
    if request.method=='POST':
        form=SignForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account have been created')
            return redirect(reverse_lazy('login'))
    else:
        form=SignForm()
    return render(request,'registrations/signup.html',{'form':form})
def send_mail(email):
    sub='Your account need to be verified'
    message=f'To verify your link click to following link.\n http://127.0.0.1:8000/ '
def success_mail(request):
    return render(request,'registrations/success.html')    
def token_send(request):
    return render(request,'registrations/token_send.html')
class UserLogin(LoginView):
    '''Display the login Form and authenticate the user'''
    form_class=LoginForm
    template_name='registrations/login.html'
    success_message='You\'ve Logged in Successfully'
@login_required
def profile(request):
    return render(request,'misc/profile.html',{'user':request.user})
    
@login_required
def dashboard(request):
    info=request.user
    name=request.user.email
    print(info)
    print(name)
    return render(request,'misc/dashboard.html',{'name':name,'user':info})


class UserLogout(LogoutView):
    template_name='registrations/logout.html'
    success_message='You\'ve Logged out Successfully'
    # extra_context={
    #     'messages':messages.success()
    # }
