from django.shortcuts import render, redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
from django.utils import timezone

# Create your views here.
def tasks(request):
    tasks = Task.objects.filter(user = request.user, datecompleted__isnull = True)
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
    
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    return render(request, 'task_detail.html',{
        'task': task
    })

def update_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'GET':
        form = TaskForm(instance=task)
        return render(request, 'update_task.html', {
            'task': task,
            'form': form
        })
    else:
        form = TaskForm(request.POST, instance=task)
        try:
            form.save()
            return redirect('task_detail', task_id=task.id)
        except ValueError:
            return render(request, 'update_task.html', {
                'task': task,
                'form': form,
                'error': "ERROR: Incorrect value"
            })

def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('tasks')

def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == 'POST':
        task.delete()
        return redirect('tasks')
