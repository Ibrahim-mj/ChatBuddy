from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('SignIn/', views.signInPage, name='SignIn'),
    path('SignUp/', views.signUpPage, name='SignUp'),
]