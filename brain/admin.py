from django.contrib import admin

from .models import Clinica
from .models import Admin
from .models import Paciente
from .models import Profissional
from .models import Trabalha_Em

admin.site.register(Clinica)
admin.site.register(Admin)
admin.site.register(Paciente)
admin.site.register(Profissional)
admin.site.register(Trabalha_Em)