from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('SignIn/', views.signInPage, name='SignIn'),
    path('SignOut/', views.signOut, name='SignOut'),
    path('SignUp/', views.signUpPage, name='SignUp'),
    path('delete-tweet/<str:pk>', views.deleteTweet, name='delete-tweet'),
    path('edit-tweet/<str:pk>', views.deleteTweet, name='edit-tweet'),
]