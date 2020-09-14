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
from applications.library.celery.task import send_reminder

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
    '''
        the class will return all the available menus, without modification to the fields
    '''
    serializer_class = MenuSerializer
    
    def get_queryset(self):
        
        return Menu.objects.all()
   
class SpecificMenuAPIView(ListAPIView):
    
    '''
        The class will use a main serializer to return a menu.
        
        Through url, a parameter will be received with the id of the menu to search along with a user id in the last field of the chain.
        
        The searched menu will go through a second serializer where the menu options and a user id will be added which is passed as a parameter through the context
        La clase utilizara un serializador principal para retornar un menu.
    '''
    
    # MenuSerializer it's a base serializer of menu
    serializer_class = MenuSerializer

    def get_queryset(self):
        
        menu = self.request.GET.get('menu','')
        response = Menu.objects.filter(
            id=menu[:-1]
        )
        # SpecificMenuSerializer is a new serializer where options like text and user id are added
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
    
    '''
        this view shows the menu selection
    '''
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
        '''
            when validating the form, the saving of the new menu is not generated immediately, this is in order to extract the uuid with which it is generated.

            then, a url is generated to be sent by slack, through an asynchronous task
        '''
        menu = form.save(
            commit=False
        )
        time.sleep(1)
        
        # url Base
        reminder_url = 'Ingresa para seleccionar nuestro menu del dia %s  http://localhost:8000/select-menu/?m=%s'  % (str(menu.date),str(menu.id))

        #Integrations with celery, for created a reminder
        send_reminder(
            message=reminder_url
        )
        
        menu.save()
        
        
        return super(CreateMenuView,self).form_valid(form)
    