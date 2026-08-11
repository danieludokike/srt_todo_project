from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def task_list(request):
    """list all tasks and handle quick task creation"""
    tasks = Task.objects.all()
    form = TaskForm()
    
    
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("taskapp:task_list")
    context = {
        "tasks": tasks,
        "form": form
    }
    return render(request, "tasks/task_list.html", context)


def task_update(request, pk):
    """Update a particular task record"""
    task = get_object_or_404(Task, pk=pk)
    form = TaskForm(instance=task)
    
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("taskapp:task_ilst")
    context = {
        "form": form,
        "task": task
        }
    return render(request, "tasks/task_update.html", context)



def task_toggle(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.completed = not task.completed
        task.save()
    return redirect("taskapp:task_list")


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":
        task.delete()
        return redirect("taskapp:task_list")
    context = {"task": task}
    return render(request, "tasks/task_confirm_delete.html", context)
