from django.shortcuts import render, redirect
from django.conf import settings
from .forms import RegisterForm

def register(request):
    form = RegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect("valid_register")

    context = {'form': form}
    return render(request, 'register.html', context)

def valid_register(request):
    return render(request, 'valid-register.html')
