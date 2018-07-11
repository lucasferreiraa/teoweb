from django.urls import path
from django.contrib.auth.views import login
from . import views

urlpatterns = [
    path('entrar/', login, {'template_name': 'login.html'}, name='login'),
    path('cadastrar/', views.register, name='register'),
]
