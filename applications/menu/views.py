from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import (
    TemplateView, 
    CreateView,
    ListView,
    DeleteView,
    UpdateView
)

from rest_framework.generics import ListAPIView
from .serializers import MenuSerializer

from .models import (
    Menu,
    Option
)
from .forms import (
    BaseOptionForm,
    BaseMenuForm
)

class CreateOptionsView(CreateView):
    
    template_name = 'menu/options/add.html'
    model = Option
    form_class = BaseOptionForm
    
    success_url = reverse_lazy('menu_app:options')
    
class ListOptionsView(ListView):
    
    template_name = 'menu/options/options.html'
    model = Option
    context_object_name = 'options'
    
class ListMenuAPIView(ListAPIView):

    serializer_class = MenuSerializer
    
    def get_queryset(self):
        
        return Menu.objects.all()
    
    
class CreateMenuView(CreateView):
    
    template_name = 'menu/add.html'
    model = Menu
    form_class = BaseMenuForm
    
    success_url = reverse_lazy('menu_app:menus')