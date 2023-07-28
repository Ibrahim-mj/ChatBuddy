from django.shortcuts import render

from .models import User, Room, Tag, Message, Tweet, Comment

def homePage(request):
    tweets = Tweet.objects.all()
    tags = Tag.objects.all()

    context = {
        'tweets': tweets,
        'tags': tags,
    }

    return render(request, 'base/home.html', context)
