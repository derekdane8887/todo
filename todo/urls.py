"""todo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth import views as auth_views
from todoapp import views as todoapp_views


admin.autodiscover()

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   
   url(r'^todo/', include('todoapp.urls'), name='todo_list'),
   url(r'^tinymce/', include('tinymce.urls')),
   #url(r'^todo_form/', todoapp_views.todo_list, name='todo_list'),
   #url(r'^$', todoapp_views.add_todo, name='add_todo'),
   ]