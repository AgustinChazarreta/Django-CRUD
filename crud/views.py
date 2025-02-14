from django.shortcuts import render, redirect
from .forms import TaskForm

# Create your views here.
def tasks(request):
    return render(request, 'tasks.html')

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