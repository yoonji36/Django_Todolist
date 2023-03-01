from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Todolist

def home(request):
    todos = Todolist.objects.all()
    return render(request, 'home.html', {'todos': todos})

def create(request):
    new_todo = Todolist()
    new_todo.content = request.POST['content']
    new_todo.date = timezone.now()
    new_todo.save()
    return redirect('home')

def delete(request,id):
    delete_todo = Todolist.objects.get(id=id)
    delete_todo.delete()
    return redirect('home')