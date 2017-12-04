from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.todo_list, name='todo_list'),
	url(r'^form/', views.add_todo, name='add_todo'),
	url(r'^list/', views.todo_list, name='todo_list_ex'),
]