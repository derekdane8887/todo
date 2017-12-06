# -*- coding: utf-8 -*-
from __future__ import unicode_literals
# Create your views here.
from models import todo
from django.shortcuts import render_to_response
from django.shortcuts import render
from .forms import TodoForm
from django.shortcuts import redirect

from django.utils import timezone
import datetime
 
 #Define our function, accept a request
def todo_list(request): 
 #ORM queries the database for all of the to-do entries.
    items = todo.objects.all() 
 #Responds with passing the object items (contains info from the DB) to the template index.html
    return render_to_response('task_list.html', {'items': items})	
	
def add_todo(request):
    form = TodoForm()
    
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('task_list.html', pk=post.pk)
    else:
        form = TodoForm()
    return render(request, 'TodoForm.html', {'form': form})	