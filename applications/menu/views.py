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

from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.renderers import JSONRenderer

from .serializers import (
    MenuSerializer,
    SpecificMenuSerializer
)

from .models import (
    Menu,
    Option
)
from .forms import (
    BaseOptionForm,
    BaseMenuForm
)

import time

class CreateOptionsView(CreateView): 
    '''
        View to create options that will be used when creating the menu.

        This view uses a base form class for options and renders an html located in templates/menu/options.

    '''
    template_name = 'menu/options/add.html'
    model = Option
    form_class = BaseOptionForm
    
    success_url = reverse_lazy('menu_app:options')
    
class ListOptionsView(ListView):
    '''
        all options are listed.
        
        template that renders: options.html
        model : Option
        
        the data is added in the options variable

    '''
    template_name = 'menu/options/options.html'
    model = Option
    context_object_name = 'options'
    
class ListMenuAPIView(ListAPIView):

    serializer_class = MenuSerializer
    
    def get_queryset(self):
        
        return Menu.objects.all()
   
class SpecificMenuAPIView(ListAPIView):
    
    serializer_class = MenuSerializer

    def get_queryset(self):
        
        menu = self.request.GET.get('menu','')
        response = Menu.objects.filter(
            id=menu[:-1]
        )
        specific_menu = SpecificMenuSerializer(
            response,
            many=True,
            context = {
                'user':menu[-1:]
            }
        ).data
        return specific_menu
    
class MainMenuView(TemplateView):
    '''
        this view renders the main menu
    '''
    template_name = 'menu/menus.html'
    
class SelectMenuView(TemplateView):
    
    template_name = 'menu/select_menu.html'
    
class UpdateMenuView(UpdateView):
    
    template_name = 'menu/update.html'
    model = Menu
    form_class = BaseMenuForm
    
    success_url = reverse_lazy('menu_app:menus')
    
class DeleteMenuView(DeleteView):
    
    tempalte_name = 'menu/delete.html'
    model = Menu    
    
    success_url = reverse_lazy('menu_app:menus')
    
class CreateMenuView(CreateView):
    
    template_name = 'menu/add.html'
    model = Menu
    form_class = BaseMenuForm
    
    success_url = reverse_lazy('menu_app:menus')
    
    def form_valid(self, form):
        
        menu = form.save(
            commit=False
        )
        time.sleep(1)
        #Integrations with celery, for created a reminder
        menu.save()
        
        
        return super(CreateMenuView,self).form_valid(form)
    