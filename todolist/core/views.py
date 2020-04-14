from django.shortcuts import render
from todolist.core.models import ToDo
from django.shortcuts import render, get_object_or_404
from todolist.core.forms import ToDoForm
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import resolve_url as r


def list(request):
    todos = ToDo.objects.all()
    return render(request, "index.html", {"todos": todos})


def detail(request, slug):
    todo = get_object_or_404(ToDo, slug=slug)
    return render(request, "todo_detail.html", {"todo": todo})

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

    todo = form.save()

    return HttpResponseRedirect(r("detail", todo.slug))


def delete(request, slug):
    todo = get_object_or_404(ToDo, slug=slug)
    todo.delete()
    return HttpResponseRedirect(r("list"))
