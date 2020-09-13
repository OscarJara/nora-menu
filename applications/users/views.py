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

from rest_framework.generics import (
    CreateAPIView
)

from .serializers import UserMenuSerializer
from rest_framework.response import Response
from rest_framework import status

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
    
class CreateUserMenuAPIView(CreateAPIView):
            
    serializer_class = UserMenuSerializer
    
    def create(self, request, *args, **kwargs):
    
        serializer = self.get_serializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            response = {}
            response['success'] = True
            response['message'] = "Registro guardado exitosamente"
            response['status'] = status.HTTP_201_CREATED
            
            return Response(response,status=status.HTTP_201_CREATED)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED) 