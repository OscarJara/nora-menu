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

from .models import (
    User,
    UserMenu
)
from .forms import BaseUserForm

from rest_framework.generics import (
    CreateAPIView,
    ListAPIView
)

from .serializers import (
    UserMenuSerializer
)

from rest_framework.response import Response
from rest_framework import status

import re

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
    
class HomeView(TemplateView):
    
    template_name = 'menu/login.html'
      
class ListUserMenuAPIView(ListAPIView):
    
    serializer_class = UserMenuSerializer
    
    def get_queryset(self):
        
        user = self.request.GET.get('user','')
        if not user or re.match(r'[0,9]',user):
            return []
        
        userModel = User.objects.filter(id=user).values('profile')
        userProfile = userModel[0]['profile']
        if userProfile == '0':
            return UserMenu.objects.all()
        else:
            return UserMenu.objects.filter(user=user)