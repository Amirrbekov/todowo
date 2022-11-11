from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def signupuser(request):
    context = {}
    register = RegisterForm()
    context['register']=register
    if request.method == "GET":
        return render(request, 'signupuser.html', context)
        
    else:
        if request.POST['password'] == request.POST["confirm"]:
            try:
                user = User.objects.create_user(request.POST["username"], password=request.POST['password'])
                user.save()
                login(request, user)
                return redirect('todo:homepage')
            except IntegrityError:
                context['error']="That username has already been taken. Please choose a new username"
                return render(request, 'signupuser.html', context)
        else:
            context['error']="Passwords did not match"
            return render(request, 'signupuser.html', context)

def signinuser(request):

    context = {}
    logform = LoginForm()
    context['logform']=logform

    if request.method == "GET":

        return render(request, "signinuser.html", context)

    else:
        user = authenticate(request, username=request.POST['username'], password = request.POST['password'])
        if user is None:
            context['error']="Username or password did not match"
            return render(request, "signinuser.html", context)
        else:
            login(request, user)
            return redirect("todo:homepage")

@login_required
def logoutuser(request):
    if request.method == "POST":
        logout(request)
        return redirect("todo:home")
    