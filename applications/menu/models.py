from django.db import models

import uuid

# Create your models here.

class Option(models.Model):
    '''
        this model only asks for one field.
        
        * description : Type CharField with max length of 200 characters, required field. (The description is one of the options to choose from within the menu)
        
        Example of description:
            'Lasagna con salsa boloseña'
       
    '''
    description = models.CharField(max_length=200)

    class Meta:
        db_table = 'option'
        verbose_name = 'option'
        verbose_name_plural = 'options'

    def __str__(self):
        return self.description

class Menu(models.Model):

    '''
        model of Menu.
           
        It has a relationship much to much, where all the options that the menu will have will be assigned.
        
        * id : Type UIIDField automatically generated, (Example of UIID: 8e55f7d6-6948-40a9-b1e7-02a35bc97fb4)
        * date: Type DateFiel, required field.
        * options: Type ManyToManyField, relationship where you can have many menu options
    '''
    id = models.UUIDField( 
        primary_key = True, 
        default = uuid.uuid4, 
        editable = False
    )     
    date = models.DateField('Fecha del menu')
    options = models.ManyToManyField(Option)

    class Meta:
        db_table = 'menu'
        verbose_name = 'menu'
        verbose_name_plural = 'menus'
        
    def __str__(self):
        return str(self.id) + ' ' + str(self.date) 