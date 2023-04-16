from django.shortcuts import render, redirect
#from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

@login_required
def inicio(request):
    return render(request, "inicio.html")

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Usuario {username} creado")
            return redirect("inicio")
    else:
        form = UserRegisterForm()
    context = {"form" : form}
    return render(request, "register.html", context)