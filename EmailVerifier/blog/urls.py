from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('signup/',views.user_sign,name='sign'),
    path('accounts/login/',views.UserLogin.as_view(),name='login'),
    path('user/profile/',views.profile,name='profile'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('user/logout/',views.LogoutView.as_view(),name='logout'),
    path('token_send/',views.token_send,name='token'),
    path('success/',views.success_mail,name='succs'),
    path('(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',views.verify,name='activate')
]
