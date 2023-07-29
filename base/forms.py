from django.contrib.auth.forms import UserCreationForm
from django import forms

from .models import User


class SignUpForm(UserCreationForm):
    birthday = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'middle_name', 'username', 'email', 'avatar', 'birthday']
        # exclude = ['host', 'participants']