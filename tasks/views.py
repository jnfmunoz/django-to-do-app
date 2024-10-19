from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'priorities': Task.PRIORITY ,'states': Task.STATUS}

    return render(request, 'task_list.html', context)

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    context = {'task': task}
    return render(request, 'task_detail.html', context)

def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('task-list')            
    else:
        form = TaskForm()
    return render(request, 'task_create.html', {'form':form})

def task_update(request, pk):
    task = Task.objects.get(pk=pk)
    form = TaskForm(request.POST, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task-list')
    else:
        print(form.errors)
    return render(request, 'task_update.html', {'task':task, 'priorities': Task.PRIORITY ,'states': Task.STATUS})

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task-list')
