# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class todo(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.
         
    name = models.CharField(max_length=100, unique=True) #Like a VARCHAR field
    description = models.TextField() #Like a TEXT field
    created = models.DateTimeField() #Like a DATETIME field
    Task_Title = models.CharField(max_length=255, blank=True)
    Task_Description	=	models.CharField(max_length=255, blank=True)
    Created	=	models.DateTimeField()
    Project	=	models.CharField(max_length=255,  blank=True)
    Department	=	models.CharField(max_length=255, blank=True)
    Priority = models.IntegerField
    Modified = models.DateTimeField()
    Task_Status = models.CharField(max_length=255, blank=True)
    Status_Description = models.CharField(max_length=255, blank=True)
    SR = models.CharField(max_length=255, blank=True)
    Working_Directory =	models.URLField(max_length=200)
    Notes = models.TextField()
    Deadline = models.DateField(auto_now=False, auto_now_add=False)
    Followup_Contact = models.CharField(max_length=255, blank=True)
    Project_Concept_Document = models.URLField(max_length=200)
    Additional_Description = HTMLField()

    def __unicode__(self): #Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created = timezone.now()
        self.modified = timezone.now()
        return super(User, self).save(*args, **kwargs)