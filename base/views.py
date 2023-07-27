from django.shortcuts import render

from .models import User, Room, Tag, Message, Tweet, Comment

def homePage(request):
    tweets = Tweet.objects.all()

    context = {
        'tweets': tweets
    }

    return render(request, 'base/home.html', context)
