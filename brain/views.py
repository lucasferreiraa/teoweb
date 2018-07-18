from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.conf import settings

from .models import Clinica
from .models import Admin
from .models import Paciente
from .models import Profissional

from .forms import Clinica_Form
from .forms import Admin_Form
from .forms import Paciente_Form
from .forms import Profissional_Form
from accounts.forms import EditAccountForm

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
@login_required
def create_clinica(request):
    form = Clinica_Form(request.POST or None)
    clinicas = list(Clinica.objects.all())
    cnpjs = [c.cnpj for c in clinicas]

    if (form.is_valid()):
        form.save()
        return redirect("list-clinica")

    context = {'form': form, 'cnpjs': cnpjs}
    return render(request, "new-clinica.html", context)

@login_required
def read_clinica(request):
    clinicas = Clinica.objects.all()
    return render(request, "list-clinica.html", {'clinicas': clinicas})

@login_required
def update_clinica(request, cnpj):
    clinica = Clinica.objects.get(cnpj=cnpj)
    form = Clinica_Form(request.POST or None, instance=clinica)
    clinicas = list(Clinica.objects.all())
    cnpjs = [c.cnpj for c in clinicas]

    if (form.is_valid()):
        Clinica.objects.get(cnpj=cnpj).delete()
        form.save()
        return redirect("list-clinica")

    context = {'form': form, 'cnpjs': cnpjs, 'clinica': clinica, 'cnpj': cnpj}
    return render(request, "new-clinica.html", context)

@login_required
def delete_clinica(request, cnpj):
    clinica = Clinica.objects.get(cnpj=cnpj)

    if (request.method == 'POST'):
        clinica.delete()
        return redirect('list-clinica')

    return render(request, "delete-clinica.html", {'clinica':clinica})


# CRUD Admin
@login_required
def create_admin(request):
    form = Admin_Form(request.POST or None)

    if (form.is_valid()):
        form.save()
        return redirect("list-admin")

    return render(request, "new-admin.html", {'form':form})

@login_required
def read_admin(request):
    admin = Admin.objects.all()
    return render(request, "list-admin.html")

@login_required
def update_admin(request, id):
    admin = Admin.objects.get(id=id)
    form = Admin_Form(request.POST or None, instance=admin)

    if (form.is_valid()):
        form.save()
        return redirect("list-admin")

    return render(request, "list-admin.html", {'admin':admin, 'form':form})

@login_required
def delete_admin(request, id):
    admin = Admin.objects.get(id=id)

    if (request.method == 'POST'):
        admin.delete()
        return redirect("list-admin")

    return render(request, "delete-admin.html", {'admin':admin})


# CRUD Paciente
@login_required
def create_paciente(request):
    form = Paciente_Form(request.POST or None)
    pacientes = list(Paciente.objects.all())
    cpfs = [p.cpf for p in pacientes]

    if (form.is_valid()):
        form.save()
        return redirect("list-paciente")

    context = {'form': form, 'cpfs': cpfs}
    return render(request, "new-paciente.html", context)

@login_required
def read_paciente(request):
    pacientes = Paciente.objects.all()
    return render(request, "list-paciente.html", {'pacientes': pacientes})

@login_required
def update_paciente(request, cpf):
    paciente = Paciente.objects.get(cpf=cpf)
    form = Paciente_Form(request.POST or None, instance=paciente)
    pacientes = list(Paciente.objects.all())
    cpfs = [p.cpf for p in pacientes]

    if (form.is_valid()):
        Paciente.objects.get(cpf=cpf).delete()
        form.save()
        return redirect("list-paciente")

    context = {'paciente': paciente, 'form': form, 'cpfs': cpfs, 'cpf': cpf}
    return render(request, "new-paciente.html", context)

@login_required
def delete_paciente(request, cpf):
    paciente = Paciente.objects.get(cpf=cpf)

    if (request.method == 'POST'):
        paciente.delete()
        return redirect("list-paciente")

    return render(request, "delete-paciente.html", {'paciente':paciente})


# CRUD Profissional
@login_required
def create_profissional(request):

    form = Profissional_Form(request.POST or None)
    profissionais = list(Profissional.objects.all())
    clinicas = list(Clinica.objects.all())
    cpfs = [p.cpf for p in profissionais]
    cnpjs = [c.cnpj for c in clinicas]

    if form.is_valid():
        form.save()
        return redirect("list-profissional")

    context = {'form': form, 'cpfs': cpfs, 'cnpjs': cnpjs}
    return render(request, "new-profissional.html", context)

@login_required
def read_profissional(request):
    profissionais = Profissional.objects.all()
    return render(request, "list-profissional.html", {'profissionais': profissionais})

@login_required
def update_profissional(request, cpf):
    profissional = Profissional.objects.get(cpf=cpf)
    form = Profissional_Form(request.POST or None, instance=profissional)
    profissionais = list(Profissional.objects.all())
    clinicas = list(Clinica.objects.all())
    cpfs = [p.cpf for p in profissionais]
    cnpjs = [c.cnpj for c in clinicas]

    if (form.is_valid()):
        Profissional.objects.get(cpf=cpf).delete()
        form.save()
        return redirect("list-profissional")

    context = {'profissional':profissional, 'form':form, 'cpfs': cpfs, 'cpf': cpf, 'cnpjs': cnpjs}
    return render(request, "new-profissional.html", context)

@login_required
def delete_profissional(request, cpf):
    profissional = Profissional.objects.get(cpf=cpf)

    if (request.method == 'POST'):
        profissional.delete()
        return redirect("list-profissional")

    return render(request, "delete-profissional.html", {'profissional':profissional})

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def edit_account(request):
    form = EditAccountForm(request.POST or None, instance=request.user)

    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}
    return render(request, 'edit_account.html', context)

def my_logout(request):
    logout(request)
    return redirect(settings.LOGOUT_URL)
