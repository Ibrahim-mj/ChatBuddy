from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass

class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f'#{self.name}'

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    tag = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    time_created = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('time_created', 'date_created')

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    time_created = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[:50]
    
    class Meta:
        ordering = ('time_created', 'date_created')