from django.contrib import admin
from django.urls import path

from . import views

app_name = 'menu_app'

urlpatterns = [
    path('add-options/',views.CreateOptionsView.as_view(),name='add_options'),
    path('options/',views.ListOptionsView.as_view(),name='options'),
    path('add-menu/',views.CreateMenuView.as_view(),name='add_menu'),
    path('API/menus/',views.ListMenuAPIView.as_view(),name='api_menu'),
    path('API/specific/',views.SpecificMenuAPIView.as_view(),name='api_specific'),
    path('menus/',views.MainMenuView.as_view(),name='menus'),
    path('delete-menu/<pk>',views.DeleteMenuView.as_view(),name='delete_menu'),
    path('update-menu/<pk>',views.UpdateMenuView.as_view(),name='update_menu'),
    path('select-menu/',views.SelectMenuView.as_view(),name='select')
    
]