from django.shortcuts import render
from todolist.core.models import ToDo
from django.shortcuts import render, get_object_or_404


def list(request):
    todos = ToDo.objects.all()
    return render(request, "index.html", {"todos": todos})


def detail(request, slug):
    todo = get_object_or_404(ToDo, slug=slug)
    return render(request, "todo_detail.html", {"todo": todo})
