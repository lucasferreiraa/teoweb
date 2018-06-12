from django.urls import path

<<<<<<< HEAD
from .views import create_clinica
from .views import read_clinica
from .views import update_clinica
from .views import delete_clinica

from .views import create_admin
from .views import read_admin
from .views import update_admin
from .views import delete_admin

from .views import create_paciente
from .views import read_paciente
from .views import update_paciente
from .views import delete_paciente

from .views import create_profissional
from .views import read_profissional
from .views import update_profissional
from .views import delete_profissional

urlpatterns = [
    path('cadastrar-clinica', create_clinica, name='new-clinica'),
    path('clinicas', read_clinica, name='list-clinica'),
    path('atualizar-clinica/<int:id>/', update_clinica, name='update-clinica'),
    path('excluir-clinica/<int:id>/', delete_clinica, name='delete-clinica'),

    path('cadastrar-admin', create_admin, name='new-admin'),
    path('admins', read_admin, name='list-admin'),
    path('atualizar-admin/<int:id>/', update_admin, name='update-admin'),
    path('excluir-admin/<int:id>/', delete_admin, name='delete-admin'),

    path('cadastrar-paciente', create_paciente, name='new-paciente'),
    path('pacientes', read_paciente, name='list-paciente'),
    path('atualizar-paciente/<int:id>/', update_paciente, name='update-paciente'),
    path('excluir-paciente/<int:id>', delete_paciente, name='delete-paciente'),

    path('cadastrar-profissional', create_profissional, name='new-profissional'),
    path('profissionais', read_profissional, name='list-profissional'),
    path('atualizar-profissional/<int:id>/', update_profissional, name='update-profissional'),
    path('excluir-paciente/<int:id>/', delete_profissional, name='delete-profissional'),

]
=======
from . import views

urlpatterns = [
    path('', views.login, name='login'),
]
>>>>>>> df0fd2a1818eaa9497bcc897b9701a2ec1eaf99d
