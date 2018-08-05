from django.urls import path
from django.contrib.auth.views import login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from . import views

urlpatterns = [
    path('entrar/', login, {'template_name': 'login.html'}, name='login'),
    path('cadastrar/', views.register, name='register'),
    path('password_reset/', password_reset, name='password_reset'),
    path('password_reset/done/', password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', password_reset_confirm, name='password_reset_confirm'),
    path('reset/done/', password_reset_complete, name='password_reset_complete'),
]
