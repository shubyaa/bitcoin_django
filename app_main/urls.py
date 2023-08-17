from unicodedata import name
from django.contrib import admin
from django.urls import path

from . import views

app_name = 'app_main'


urlpatterns = [
    path('', view=views.index, name='index'),
    path('comments/', views.comments, name='comments'),   
]
