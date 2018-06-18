from django.contrib import admin

from .models import Simulacion,DatoEntrada,VariableMacro

# Register your models here.
admin.site.register(Simulacion)
admin.site.register(DatoEntrada)
admin.site.register(VariableMacro)