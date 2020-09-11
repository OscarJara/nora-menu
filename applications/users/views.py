from django.shortcuts import render

from .models import User

from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView
)

from .models import User
from .forms import CreateUser


class CreateUserView(CreateView):
    
    template_name = 'users/add.html'
    model = User
    form_class = CreateUser
    
    success_url = reverse_lazy('user_app:home')
    

        