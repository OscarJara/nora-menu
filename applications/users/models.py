from django.db import models
from model_utils.models import TimeStampedModel
from applications.menu.models import Menu

import datetime
    
class User(models.Model):
    
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
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
    def __str__(self):
        
        return str(self.profile) + ' ' + self.full_name + ' ' + self.mail + ' ' + self.password
    
class UserMenu(models.Model):
    
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