import uuid
from django.conf import settings
from django.shortcuts import redirect, render
from django.views.generic.detail import DetailView
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.mail import send_mail

from blog.models import CustomUser, Profile
from blog.forms import LoginForm, SignForm
# Create your views here.
def home(request):
    return render(request,'misc/home.html')
def about(request):
    return render(request,'misc/about.html')    
def user_sign(request):
    user=get_user_model()
    if request.method=='POST':
        form=SignForm(request.POST)
        email=request.POST.get('email')
        if form.is_valid():
            user=form.save(commit=False)
            user.is_active=False
            print(user.email)
            user.save()
            auth_token=str(uuid.uuid4())
            # profile_obj=Profile.objects.create()
            send_email(email=user.email,token=auth_token)
            messages.success(request,'Your account have been created')
            return redirect(reverse_lazy('login'))
    else:
        form=SignForm()
    return render(request,'registrations/signup.html',{'form':form})
def verify(request,token):
    try:
        user_obj=CustomUser.objects.filter(auth_token=token).first()
        if user_obj:
            user_obj.is_verified=True
            user_obj.sav e()
            messages.success(request,"Your Account has been verified.")
            return redirect(reverse_lazy(UserLogin))
    except Exception as e:
        pass


def send_email(email,token):
    sub='Your account need to be verified'
    message=f'To verify your link click to following link.\n http://127.0.0.1:8000/{token} '
    sender=settings.EMAIL_HOST_USER
    recipent_list=[email]
    send_mail(subject=sub,message=message,from_email=sender,recipient_list=recipent_list)

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



'''
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.core.mail import send_mail

def signup(request):
    User = get_user_model()
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            if Yourmodel.objects.filter(email__iexact=email).count() == 1:
                user = form.save(commit=False)
                user.is_active = False
                user.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your account.'
                message = render_to_string('email_template.html', {
                            'user': user,
                            'domain': current_site.domain,
                            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                            'token': account_activation_token.make_token(user),
                        })
                to_email = form.cleaned_data.get('email')
                send_mail(mail_subject, message, 'youremail', [to_email])
                return HttpResponse('Please confirm your email address to complete the registration')
     else:
        form = SignupForm()
    return render(request, 'regform.html', {'form': form})

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')






'''



# token generator
# '''
# 





# signals
'''
from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string

from .token_generator import generate_token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def send_verify_email(instance, created, **kwargs):
    if not created or instance.is_active:
        return
    domain = settings.ALLOWED_HOSTS[0] or 'http://localhost:8000'
    token = generate_token(instance.id)
    message = render_to_string(
        "users/verify_email.html",
        context={"token": token, "base_url": domain},
    )
    send_mail(
        "Verify Email Subject",
        message=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[instance.email],
    )

'''


# Views


'''
from django.contrib.auth import get_user_model
from .token_generator import BadToken , ExpiredToken , validate_token
rom django.views import View

class EmailVerify(View):

    def get(self, request : HttpRequest) -> HttpResponse:
        UserModel = get_user_model()
        token = request.GET.get('token')
        if not token:
            return HttpResponseBadRequest('Error')
        try:
            user_id = validate_token(token)
        except BadToken:
            return HttpResponseBadRequest('Error')
        except ExpiredToken:
            return HttpResponseBadRequest('Error')
        user = UserModel.objects.get(pk=user_id)
        if user.email_verified:
            return HttpResponseBadRequest('Error')
        user.is_active = True
        user.save()
        return HttpResponse('Your account has been activated')'''



'''{% autoescape off %}  
Hi {{ user.username }},  
Please click on the link to confirm your registration,  
http://{{ domain }}{% url 'activate' uidb64=uid token=token %}  
{% endautoescape %} '''        




'''    def activate(request, uidb64, token):  
        User = get_user_model()  
        try:  
            uid = force_text(urlsafe_base64_decode(uidb64))  
            user = User.objects.get(pk=uid)  
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
            user = None  
        if user is not None and account_activation_token.check_token(user, token):  
            user.is_active = True  
            user.save()  
            return HttpResponse('Thank you for your email confirmation. Now you can login your account.')  
        else:  
            return HttpResponse('Activation link is invalid!')  '''

'''    from django.urls import path  
    from .views import home, index, activate  
    urlpatterns = [  
        path('', home, name = 'home'),  
        path('form/', index, name = 'index'),  
        path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
            activate, name='activate'),  
    ]  '''