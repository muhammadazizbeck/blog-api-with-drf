from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm,UserChangeForm

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser