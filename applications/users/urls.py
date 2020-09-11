from django.urls import include, path

from . import views

app_name = 'user_app'

urlpatterns = [
    path('add-user/', views.CreateUserView.as_view(),name='add'),
    path('home-user/', views.ListUserView.as_view(),name='home'),
    path('delete-user/<pk>', views.UserDeleteView.as_view(),name='delete'),
    path('update-user/<pk>', views.UpdateUserView.as_view(),name='update')
]
