from django.urls import include, path

from . import views

app_name = 'user_app'

urlpatterns = [
    path('add-user/', views.CreateUserView.as_view(),name='add'),
    path('home-user/', views.ListUserView.as_view(),name='home'),
    path('delete-user/<pk>', views.UserDeleteView.as_view(),name='delete'),
    path('update-user/<pk>', views.UpdateUserView.as_view(),name='update'),
    path('API/add-select/',views.CreateUserMenuAPIView.as_view(),name='user_name'),
    path('API/user-menu/',views.ListUserMenuAPIView.as_view(),name='user_menu'),
    path('menus-selected',views.SelectMenuListView.as_view(),name='menus_selected'),
]
