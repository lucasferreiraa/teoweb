from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar-clinica', views.create_clinica, name='new-clinica'),
    path('clinicas', views.read_clinica, name='list-clinica'),
    path('atualizar-clinica/<cnpj>/', views.update_clinica, name='update-clinica'),
    path('excluir-clinica/<cnpj>/', views.delete_clinica, name='delete-clinica'),

    path('cadastrar-admin', views.create_admin, name='new-admin'),
    path('admins', views.read_admin, name='list-admin'),
    path('atualizar-admin/<int:id>/', views.update_admin, name='update-admin'),
    path('excluir-admin/<int:id>/', views.delete_admin, name='delete-admin'),

    path('cadastrar-paciente', views.create_paciente, name='new-paciente'),
    path('pacientes', views.read_paciente, name='list-paciente'),
    path('atualizar-paciente/<int:id>/', views.update_paciente, name='update-paciente'),
    path('excluir-paciente/<int:id>', views.delete_paciente, name='delete-paciente'),

    path('cadastrar-profissional', views.create_profissional, name='new-profissional'),
    path('profissionais', views.read_profissional, name='list-profissional'),
    path('atualizar-profissional/<cpf>/', views.update_profissional, name='update-profissional'),
    path('excluir-paciente/<cpf>/', views.delete_profissional, name='delete-profissional'),

    path('', views.index, name='index'),
    path('editar_conta/', views.edit_account, name='edit_account'),
    path('logout/', views.my_logout, name='logout'),
]
