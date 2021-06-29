from . import views
from django.contrib import admin
from django.urls import path

app_name = 'TennisApp'
urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', views.signup, name ='signup'),
    path('signup_add/', views.signup, name ='signup_add'),
]
