from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.core.exceptions import ValidationError



# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/index')
    else:
            form = RegisterForm()

    return render(response, "register/register.html", {"form": form})