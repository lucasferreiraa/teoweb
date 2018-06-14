from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse

from .models import Clinica
from .models import Admin
from .models import Paciente
from .models import Profissional

from .forms import Clinica_Form
from .forms import Admin_Form
from .forms import Paciente_Form
from .forms import Profissional_Form

'''
Atualizando branch
Os arquivos HTML que estão sendo chamados nas funções não existem.
O dev front-end deve criá-los e tomar como guia o código desse arquivo,
para que as funções possam chamar seus respectivos arquivos e que as urls
sejam criadas corretamente.
Por segurança, não crie os HTMLs das funções do admin, pois isso precisa ser visto
se vai ficar visível para o cliente.
'''

# CRUD Clinica
def create_clinica(request):
    form = Clinica_Form(request.POST or None)

    if (form.is_valid()):
        form.save()
        return redirect("list-clinica")

    return render(request, "new-clinica.html", {'form':form})


def read_clinica(request):
    clinicas = Clinica.objects.all()
    linha = True
    return render(request, "list-clinica.html", {'clinicas':clinicas, 'linha': linha})


def update_clinica(request, id):
    clinica = Clinica.objects.get(id=id)
    form = Clinica_Form(request.POST or None, instance=clinica)

    if (form.is_valid()):
        form.save()
        return redirect("list-clinica")

    return render(request, "list-clinica.html", {'clinica':clinica, 'form':form})


def delete_clinica(request, id):
    clinica = Clinica.objects.get(id=id)

    if (request.method == 'POST'):
        clinica.delete()
        return redirect('list-clinica')

    return render(request, "delete-clinica.html", {'clinica':clinica})


# CRUD Admin

def create_admin(request):
    form = Admin_Form(request.POST or None)

    if (form.is_valid()):
        form.save()
        return redirect("list-admin")

    return render(request, "new-admin.html", {'form':form})


def read_admin(request):
    admin = Admin.objects.all()
    return render(request, "list-admin.html")


def update_admin(request, id):
    admin = Admin.objects.get(id=id)
    form = Admin_Form(request.POST or None, instance=admin)

    if (form.is_valid()):
        form.save()
        return redirect("list-admin")

    return render(request, "list-admin.html", {'admin':admin, 'form':form})


def delete_admin(request, id):
    admin = Admin.objects.get(id=id)

    if (request.method == 'POST'):
        admin.delete()
        return redirect("list-admin")

    return render(request, "delete-admin.html", {'admin':admin})


# CRUD Paciente

def create_paciente(request):
    form = Paciente_Form(request.POST or None)

    if (form.is_valid()):
        form.save()
        return redirect("list-paciente")

    return render(request, "new-paciente.html", {'form':form})


def read_paciente(request):
    paciente = Paciente.objects.all()
    return render(request, "list-paciente.html")


def update_paciente(request, id):
    paciente = Paciente.objects.get(id=id)
    form = Paciente_Form(request.POST or None, instance=paciente)

    if (form.is_valid()):
        form.save()
        return redirect("list-paciente")

    return render(request, "list-paciente.html", {'paciente':paciente, 'form':form})


def delete_paciente(request, id):
    paciente = Paciente.objects.get(id=id)

    if (request.method == 'POST'):
        paciente.delete()
        return redirect("list-paciente")

    return render(request, "delete-paciente.html", {'paciente':paciente})


# CRUD Profissional

def create_profissional(request):

    form = Profissional_Form(request.POST or None)

    if (form.is_valid()):
        form.save()
        return redirect("login")

    return render(request, "new-profissional.html", {'form': form})


def read_profissional(request):
    profissional = Profissional.objects.all()
    return render(request, "list-profissional.html", {'profissional':profissional})


def update_profissional(request, id):
    profissional = Profissional.objects.get(id=id)
    form = Profissional_Form(request.POST or None, instance=profissional)

    if (form.is_valid()):
        form.save()
        return redirect("list-profissional")

    return render(request, "list-profissional.html", {'profissional':profissional, 'form':form})


def delete_profissional(request, id):
    profissional = Profissional.objects.get(id=id)

    if (request.method == 'POST'):
        profissional.delete()
        return redirect("list-profissional")

    return render(request, "delete-profissional.html", {'profissional':profissional})

def login(request):
    return render(request, 'login.html')
