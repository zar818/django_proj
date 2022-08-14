from .models import ArtWork, Article
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from .forms import ArtworkForm, SignupForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
# Create your views here.

def home(request):
    img=ArtWork.arts.all()
    return render(request,'all/home.html',{'img':img})
class Articles(ListView):
    model=Article
    template_name='all/article.html'
    context_object_name='articles'
@login_required
def img_uploader(request):
    if request.method=='POST':
        form=ArtworkForm(request.POST,request.FILES,request.user)
        if form.is_valid():
            form.instance.user=request.user
            form.save()
            messages.success(request,'Your ArtWork has been uploaded.')
    else:
        form=ArtworkForm()
    return render(request,'all/art_uploader.html',{'form':form})
@login_required
def profile(request):
    data=ArtWork.arts.filter(user=request.user)
    data2=Article.objects.filter(user=request.user)
    data3=request.user.username
    context={
        'd1':data,
        'd2':data2,
        'd3':data3
    }
    return render(request,'all/profile.html',context)
class SignUpView(FormView):
    form_class=SignupForm
    success_url=reverse_lazy('login')
    template_name='all/signup.html'
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
class LogInView(LoginView):
    template_name='all/login.html'

