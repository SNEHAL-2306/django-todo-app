from django.shortcuts import render, redirect, get_object_or_404
from .models import Task

def task_list(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        print("Received title:", title)
        if title:
            Task.objects.create(title=title)
        return redirect('task_list')

    tasks = Task.objects.all()
    return render(request, 'myapp/task_list.html', {'tasks': tasks})

def edit_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        title = request.POST.get('title')
        task.title = title
        task.save()
        return redirect('task_list')
    return render(request, 'myapp/edit_task.html', {'task': task})

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.delete()
    return redirect('task_list')

def toggle_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')