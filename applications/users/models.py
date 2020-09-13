from django.db import models
from model_utils.models import TimeStampedModel
from applications.menu.models import Menu

import datetime
from django.core.exceptions import ValidationError
    
class User(models.Model):
    
    '''
        Main model for the Users, fields are managed to later add menu selection.
        
        * full_name : Type CharField with max length of 100 characters, required field
        * mail : Type EmailField, required field.
        * password : Type Charfield with max length of 120, required field.
        * profile : Type Charfield with max length of 1.
                    The profiles are added inside a variable PROFILE_CHOISES, in a which a selection is generated
        
    '''
    PROFILE_CHOISES = (
        ('0','Administrador'),
        ('1','Trabajador'),
    )    
    full_name = models.CharField('Nombre Completo', max_length=100)
    mail = models.EmailField('Email')
    password = models.CharField('Contraseña', max_length=100)
    profile = models.CharField(
        'Perfil',
        max_length=1,
        choices=PROFILE_CHOISES
    )
    
    class Meta:
        # user is the name of the table in database
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
    def __str__(self):
        # return default full_name of the User
        return self.full_name
    
class UserMenu(models.Model):
    
    '''
        Main model for the UserMenus.
        
        * user : Type ForeignKey relation with User model, required field
        * menu : Type ForeignKey relation with Menu model, required field.
        * observation : Type Charfield with max length of 200, required field. (observation regarding the selected menu, for example: 'La ensalada sin tomate')
        * option : Type IntegerField, required field. (is the id of the menu option that the user chose)
        * date: Type DateField is not required, default value is now.        
    '''
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE
    )
    observation = models.CharField(max_length=200)
    option = models.IntegerField()
    date = models.DateField(default=datetime.datetime.utcnow)
    
    class Meta:
        db_table = 'userMenu'
        verbose_name = 'userMenu'
        verbose_name_plural = 'userMenu'
        
    def __strt__(self):
        
        return self.observation