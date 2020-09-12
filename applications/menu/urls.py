from django.contrib import admin
from django.urls import path

from . import views

app_name = 'menu_app'

urlpatterns = [
    path('add-options/',views.CreateOptionsView.as_view(),name='add_options'),
    path('options/',views.ListOptionsView.as_view(),name='options'),
    # path('menus/',views.ListMenusView.as_view(),name='menus'),
    path('add-menu/',views.CreateMenuView.as_view(),name='add_menu'),
    path('API/menus/',views.ListMenuAPIView.as_view(),name='menus'),
]

# urlpatterns = [
#     path('add-user/', views.CreateUserView.as_view(),name='add'),
#     path('home-user/', views.ListUserView.as_view(),name='home'),
#     path('delete-user/<pk>', views.UserDeleteView.as_view(),name='delete'),
#     path('update-user/<pk>', views.UpdateUserView.as_view(),name='update')
# ]
