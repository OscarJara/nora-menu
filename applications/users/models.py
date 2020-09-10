from django.db import models
from model_utils.models import TimeStampedModel
from applications.menu.models import Menu

import datetime

class Profile(models.Model):
        
    name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'profile'
        verbose_name = 'profile'
        verbose_name_plural = 'profiles'
    
    def __str__(self):
        
        return self.name + ' : ' + str(self.is_active)

class User(TimeStampedModel):
    
    full_name = models.CharField(max_length=100)
    mail = models.EmailField()
    password = models.CharField(max_length=100)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE
    )
    
    class Meta:
        db_table = 'user'
        verbose_name = 'user'
        verbose_name_plural = 'users'
        
    def __str__(self):
        
        return self.full_name
    
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