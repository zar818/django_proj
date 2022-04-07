from django.urls import path
from .import views


urlpatterns = [
    path('',views.home,name='home'),
    path('upload/art/',views.img_uploader,name='img_upload'),
    path('article/',views.Articles.as_view(),name='articles'),
    path('signup/',views.SignUpView.as_view(),name='signup'),
    path('login/',views.LogInView.as_view(),name='login'),
    path('accounts/profile/',views.profile,name='profile')


]
