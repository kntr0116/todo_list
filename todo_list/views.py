from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Todo

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    return render(request, 'todo_list/index.html', {'todos': todos})

def add(request):
    todo = Todo(text=request.POST['text'])
    todo.save()
    return HttpResponseRedirect(reverse('todo_list:index', args=()))

def remove(request, todo_id):
    todo = get_object_or_404(Todo, pk=todo_id)
    todo.delete()
    return HttpResponseRedirect(reverse('todo_list:index', args=()))