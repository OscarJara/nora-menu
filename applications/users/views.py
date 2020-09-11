from django.shortcuts import render

from .models import User

from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
)

from .models import User
from .forms import BaseUserForm


class CreateUserView(CreateView):
    
    template_name = 'users/add.html'
    model = User
    form_class = BaseUserForm
    
    success_url = reverse_lazy('user_app:home')
    
class ListUserView(ListView):

    template_name = 'users/users.html'
    model = User
    context_object_name = 'users'
        
class UserDeleteView(DeleteView):
    
    template_name = "users/delete.html"
    model = User
    success_url = reverse_lazy('user_app:home')


class UpdateUserView(UpdateView):
    template_name = "users/update.html"
    model = User
    form_class = BaseUserForm
    success_url = reverse_lazy('user_app:home')