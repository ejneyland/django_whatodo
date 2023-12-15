# myapp/views.py
from django.shortcuts import render, redirect
from .forms.form_task import TaskForm
from .models.model_task import Task

def home(request):
    return render(request, "home.html")

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(
                "list_tasks"
            )
    else:
        form = TaskForm()

    return render(request, "create_task.html", {"form": form})


def list_tasks(request):
    tasks = Task.objects.all()
    return render(request, "list_tasks.html", {"tasks": tasks})
