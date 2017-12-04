# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# Create your views here.
from models import todo
from django.shortcuts import render_to_response
 
def index(request): #Define our function, accept a request
 
    items = todo.objects.all() #ORM queries the database for all of the to-do entries.
 
    return render_to_response('index.html', {'items': items}) #Responds with passing the object items (contains info from the DB) to the template index.html
