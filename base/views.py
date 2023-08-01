from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

from .models import User, Room, Tag, Message, Tweet, Comment
from .forms import SignUpForm

def homePage(request):
    tweets = Tweet.objects.all()
    tags = Tag.objects.all()

    context = {
        'tweets': tweets,
        'tags': tags,
    }

    return render(request, 'base/home.html', context)

def explorePage(request):
    pass

def signInPage(request):
    page = 'login'

    # if request.user.is_authenticated:
    #     return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)

        except:
            messages.error(request, 'Email not found')

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.error(request, 'Email or Password incorrect')

    context = {
        'page': page
    }
    return render(request, 'base/signin_signup.html', context)

def signOut(request):
    logout(request)

    return redirect('home')

def signUpPage(request):
    form = SignUpForm()

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.first_name = user.first_name.title()
            user.last_name = user.last_name.title()
            user.save()
            login(request, user)

            return redirect('home')
        else:
            messages.error(request, 'An error occurred while signing up')

    context = {
        'form': form,
    }

    return render(request, 'base/signin_signup.html', context)

@login_required(login_url='/login')
def deleteTweet(request, pk):
    tweet = Tweet.objects.get(id=pk)
    if request.method == 'POST':
        tweet.delete()
        return redirect('home')

    context = {
        'obj': tweet
    }

    return render(request, 'base/delete.html', context)

# def deleteTweet(request, pk):
#     tweet = Tweet.objects.get(id=pk)
#     if request.method == 'POST':
        