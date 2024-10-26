from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskCreateForm, TaskUpdateForm

# Create your views here.
def task_list(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks, 'priorities': Task.PRIORITY}

    return render(request, 'tasks/task_list.html', context)

def task_detail(request, pk):
    task = Task.objects.get(pk=pk)
    context = {'task': task}
    return render(request, 'tasks/task_detail.html', context)

def task_create(request):
    if request.method == 'POST':
        form = TaskCreateForm(request.POST)
        if form.is_valid():
            form.save()            
            return redirect('task-list')            
    else:
        form = TaskCreateForm()
    return render(request, 'tasks/task_create.html', {'form':form})

def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)
    
    if request.method == 'POST':
        form = TaskUpdateForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskUpdateForm(instance=task)

    return render(request, 'tasks/task_update.html', {
        'form': form,
        'task': task
    })

def task_delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task-list')
