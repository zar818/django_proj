from os import name
from django.urls import path
from .import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('issues/',views.issues,name='issues'),
    path('signup/',views.signingup,name='signup'),
    path('login/',views.loggingin,name='loggingin'),
    path('logout/',views.loggingout,name='loggingout'),
    path('profile/',views.editprofile,name='profile'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('addpost/',views.addpost,name='addpost'),
    path('updatepost/<id>/',views.updatepost,name='updatepost'),
    path('delete/<id>',views.deletepost,name='delete'),
    path('changePassword/',views.ch_password,name='changepass'),
    path('contact/',views.contact,name='contact'),


]
