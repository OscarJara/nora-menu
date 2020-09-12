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

import json
import time

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
   
class SpecificMenuAPIView(ListAPIView):
    
    print ('INSTANCIA POR PRIMERA VEZ SIN CONTEXT')
    # serializer_class = SpecificMenuSerializer
    serializer_class = MenuSerializer

    def get_queryset(self):
        
        print ('ENTRA AL QUERY SET')
        menu = self.request.GET.get('menu','')
        print ('SE BUSCA MENU')
        
        response = Menu.objects.filter(
            id=menu[:-1]
        )
        print (' New Serializer')
        specific_menu = SpecificMenuSerializer(
            response,
            many=True,
            context = {
                'user':menu[-1:]
            }
        ).data
        print (specific_menu)
        return specific_menu
    
class MainMenuView(TemplateView):
    template_name = 'menu/menus.html'
    
    
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
    