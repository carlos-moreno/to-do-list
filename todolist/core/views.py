from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.shortcuts import resolve_url as r

from todolist.core.forms import ToDoForm
from todolist.core.models import ToDo
from datetime import date


def list(request):
    todos = ToDo.objects.filter(ended=False)
    todos_done = ToDo.objects.filter(ended=True)
    return render(request, "index.html", {"todos": todos, "todos_done": todos_done})


def new(request):
    if request.method == "POST":
        return create(request)

    return empty_form(request)


def empty_form(request):
    return render(
        request, "todo_create.html", {"form": ToDoForm()}
    )


def create(request):
    form = ToDoForm(request.POST)

    if not form.is_valid():
        return render(request, "todo_create.html", {"form": form})

    form.save()

    return HttpResponseRedirect(r("list"))


def delete(request, slug):
    todo = get_object_or_404(ToDo, slug=slug)
    todo.delete()
    return HttpResponseRedirect(r("list"))


def done(request, slug):
    todo = get_object_or_404(ToDo, slug=slug)
    todo.ended = True
    todo.ended_in = date.today()
    todo.save(update_fields=['ended', 'ended_in'])
    return HttpResponseRedirect(r("list"))
