from unicodedata import name
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'accounts'


urlpatterns = [ 
    path('', views.loginPage, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logoutPage, name='logout'),
    path('send_mail/<uidb64>/<token>',views.send_mail, name='send_mail'),
    path('profile/', views.user_profile, name='profile'),   

    ]


