from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import TodoForm
from .models import Todo
from django.utils import timezone

# Create your views here.

def home_view(request):

    return render(request, 'home.html')

@login_required
def createtodo_view(request):

    context = {}
    todoform = TodoForm()
    context['todoform'] = todoform
    if request.method == "GET":
        return render(request, 'createtodo.html', context)
    else:
        try:
            form = TodoForm(request.POST)
            newtodo = form.save(commit=False)
            newtodo.user = request.user
            newtodo.save()
            return redirect("todo:homepage")
        except ValueError:
            context['error'] = "Bad data passed in. Try again"
            return render(request, "createtodo.html", context)

@login_required
def homepage_view(request):
    context = {}
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=True)       
    context['todos']=todos
    return render(request, "homepage.html", context)

@login_required
def completedtodos_view(request):
    context = {}
    todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    context['todos']=todos
    return render(request, "completedtodos.html", context)

@login_required
def viewtodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    form = TodoForm(instance=todo)
    context = {}
    context['todo']=todo
    context['form']=form
    if request.method == "GET":
        return render(request, "viewtodo.html", context)
    else:
        try:
            form = TodoForm(request.POST, instance=todo)
            form.save()
            return redirect("todo:homepage")
        except ValueError:
            context['error']= "Bad info"
            return render(request, "viewtodo.html", context)

@login_required
def completetodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == "POST":
        todo.datecompleted= timezone.now()
        todo.save()
        return redirect("todo:homepage")

@login_required
def deletetodo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    if request.method == "POST":
        todo.delete()
        return redirect("todo:homepage")