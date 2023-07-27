from django.contrib import admin

from .models import User, Tag, Room, Message, Tweet, Comment

admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Room)
admin.site.register(Message)
admin.site.register(Tweet)
admin.site.register(Comment)