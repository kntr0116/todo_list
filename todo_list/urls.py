from django.urls import path

from . import views

app_name = 'todo_list'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<int:todo_id>/remove/', views.remove, name='remove'),
]