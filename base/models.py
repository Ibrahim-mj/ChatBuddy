from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    middle_name = models.CharField(max_length=200, null=True, blank=True)
    username = models.CharField(max_length=200, null=True)
    # display_name = models.CharField(max_length=200, null=True, blank=True, default=username)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, default='avatar.svg')
    date_joined = models.DateTimeField(auto_now_add=True)
    birthday = models.DateField(null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name',]

    def __str__(self) -> str:
        return f'@{self.username.title()}'
    
    # def default_name(self):
    #     if self.display_name is not str:
    #         return self.first_name
    #     return self.display_name

# class Follow(models.Model):
#     pass
class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        if self.name[0] == '#':
            return self.name
        return f'#{self.name}'

    class Meta:
        ordering = []


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
            return self.name

    # class Meta:
    #     ordering = []

# I will add interests/topics later(for both tweets and rooms)

class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    participants = models.ManyToManyField(User, related_name='participants', blank=True)
    time_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ('time_modified', 'date_created')

class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, null=True)
    time_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.body[:50]
    
    class Meta:
        ordering = ('time_modified', 'date_created')

class Tweet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, null=True, blank=True)
    time_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.FileField(null=True, blank=True)

    class Meta:
        ordering = ('time_modified', 'date_created')

    def __str__(self) -> str:
        return self.body[:20]

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, null=True)
    body = models.TextField()
    time_modified = models.DateTimeField(auto_now=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('time_modified', 'date_created')

    def __str__(self) -> str:
        return self.body[:20]


# class Reactions(models.Model):
#     pass

# class Retweet(models.Model):
#     pass