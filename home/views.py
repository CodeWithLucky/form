from django.shortcuts import render, redirect
from home.forms import TaskForm
from . models import Task

# Create your views here.
def index(request):
    data = Task.objects.all()
    return render(request, 'index.html', {'data': data})

def create(request):
    if request.method == "POST":
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('index')
    form = TaskForm()
    return render(request, 'create.html', {'form' : form})

def update(request, id):
    task = Task.objects.get(id = id)
    if request.method == 'POST':
        task_form = TaskForm(request.POST, instance=task)
        if task_form.is_valid():
            task_form.save()
            return redirect('index')
    task_form = TaskForm(instance=task)
    return render(request, 'create.html', {'form':task_form})


def delete(request, id):
    task = Task.objects.get(id = id)
    task.delete()
    return redirect('index')

