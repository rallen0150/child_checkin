from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User



class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = "/"
