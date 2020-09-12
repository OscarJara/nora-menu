from django.db import models

import uuid

# Create your models here.

class Option(models.Model):
    
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'option'
        verbose_name = 'option'
        verbose_name_plural = 'options'

    def __str__(self):
        return self.description

class Menu(models.Model):

    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
    )     
    date = models.DateField()
    options = models.ManyToManyField(Option)

    class Meta:
        db_table = 'menu'
        verbose_name = 'menu'
        verbose_name_plural = 'menus'
        
    def __str__(self):
        return str(self.id) + ' ' + str(self.date) + ' ' + str(self.options)