from django.urls import path
from .import views
urlpatterns = [
    path('',views.home,name='home'),
    path('dashboard/',views.user_dash_board,name='dashboard'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update'),
]
