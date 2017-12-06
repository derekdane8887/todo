# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from tinymce.models import HTMLField
from datetime import date, datetime, timedelta
from django.utils import timezone
# Create your models here.
class todo(models.Model): #Table name, has to wrap models.Model to get the functionality of Django.
         
    name = models.CharField(max_length=100, unique=True) #Like a VARCHAR field
    description = models.TextField() #Like a TEXT field
    created = models.DateTimeField() #Like a DATETIME field
    Task_Title = models.CharField(max_length=255, blank=True)
    Task_Description	=	models.CharField(max_length=255, blank=True)
    Project	= models.CharField(max_length=255,  blank=True)
    Department = models.CharField(max_length=255, blank=True)
    Priority = models.IntegerField
    Modified = models.DateTimeField(null=True)
    Task_Status = models.CharField(max_length=255, blank=True)
    Status_Description = models.CharField(max_length=255, blank=True)
    SR = models.CharField(max_length=255, blank=True)
    Working_Directory =	models.URLField(max_length=200,null=True)
    Notes = models.TextField(blank=True)
    Deadline = models.DateField(null=True, blank=True)
    Followup_Contact = models.CharField(max_length=255, blank=True)
    Project_Concept_Document = models.URLField(max_length=200,null=True)
    #Additional_Description = HTMLField()

    def __unicode__(self): #Tell it to return as a unicode string (The name of the to-do item) rather than just Object.
        return self.name
   