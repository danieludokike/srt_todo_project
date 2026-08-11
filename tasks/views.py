from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm


def task_lsit(request):
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
    return render(request, "task/task_list.html", context)
