from django.shortcuts import render, redirect
from .forms import TaskForm
from .models import Task

# Create your views here.
def tasks(request):
    tasks = Task.objects.filter(user = request.user)
    return render(request, 'tasks.html',{
        'tasks': tasks
    })

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html',{
            'form': TaskForm
        })
    else:
        form = TaskForm(request.POST)
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.save()
        return redirect('tasks')