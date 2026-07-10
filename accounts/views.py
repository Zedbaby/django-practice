from django.shortcuts import render , redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .forms import ChangeUserForm

def signup(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("login")
    context = {"form": form}
    return render(request , "registration/signup.html" , context)

def change_user_info(request):
    form = ChangeUserForm()
    if request.method == "POST":
        form = ChangeUserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("blogpost:home")
    context = {"form": form}
    return render(request , "registration/change_user_info.html" , context)